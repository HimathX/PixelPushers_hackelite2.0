from fastapi import APIRouter, HTTPException, Query, Body, BackgroundTasks
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
import logging
import uuid
from schemas import (
    RSSExtractionRequest, 
    RSSExtractionResponse,
    Article
)
from utils.data_collection.rss_extractor import RSSExtractor
from core.database import article_collection

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create router
router = APIRouter(tags=["rss-extraction"])

# Store extraction tasks (in-memory for simplicity)
extraction_tasks = {}

# Default feed URLs
feed_urls = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://www.france24.com/en/rss",
    "https://www.rt.com/rss/news/",
    "https://www.cgtn.com/subscribe/rss/section/world.xml",
    "https://feeds.reuters.com/reuters/topNews",
    "https://www.aljazeera.com/xml/rss/all.xml"
]

@router.post("/extract", response_model=RSSExtractionResponse)
async def extract_rss_feeds(request: RSSExtractionRequest):
    """
    Extract articles from RSS feeds and store them in the database
    """
    try:
        extractor = RSSExtractor()
        
        from_date = request.from_date
        to_date = request.to_date
        
        logger.info(f"Starting RSS extraction for {len(feed_urls)} feeds")
        logger.info(f"Date range: {from_date} to {to_date}")
        
        # Process feeds
        all_articles = await extractor.process_feeds(
            feed_urls=feed_urls,
            from_date=from_date,
            to_date=to_date,
            max_articles=request.max_articles,
            strip_html=request.strip_html,
            fetch_full_content=request.fetch_full_content,
            remove_duplicates=request.remove_duplicates,
            include_metadata=request.include_metadata,
            verbose=request.verbose
        )
        
        # Build list of Article models and store in database
        articles_out: List[Article] = []
        stored_count = 0
        skipped_count = 0
        
        for article_data in all_articles:
            try:
                article = Article(
                    title=article_data.get('title', ''),
                    content=article_data.get('content', ''),
                    url=article_data.get('url'),
                    published_at=article_data.get('published_date'),
                    source=article_data.get('author'),
                    image_url=article_data.get('image_url')
                )
                
                # Convert to dict for MongoDB
                article_dict = article.dict()
                article_dict["extracted_at"] = datetime.now()
                
                # Check for duplicates by URL or title before inserting
                existing = article_collection.find_one({
                    "$or": [
                        {"url": article_dict["url"]},
                        {"title": article_dict["title"]}
                    ]
                })
                
                if existing:
                    logger.info(f"Skipping duplicate article: {article_dict['title']}")
                    skipped_count += 1
                    continue
                
                # Insert into MongoDB
                result = article_collection.insert_one(article_dict)
                if result.inserted_id:
                    logger.info(f"Stored article: {article_dict['title']}")
                    stored_count += 1
                    articles_out.append(article)
                
            except Exception as e:
                logger.warning(f"Error processing article: {e}")
                continue

        return RSSExtractionResponse(
            success=True,
            message=f"Successfully extracted {len(all_articles)} articles, stored {stored_count}, skipped {skipped_count} duplicates",
            articles=articles_out,
            total_articles=len(all_articles),
            articles_stored=stored_count,
            articles_skipped=skipped_count
        )
    except Exception as e:
        logger.error(f"Failed to extract RSS feeds: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to extract RSS feeds: {str(e)}"
        )

