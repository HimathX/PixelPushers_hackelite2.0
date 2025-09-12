# InFact Platform (Backend)

A FastAPI application that processes news articles to remove sensationalism through AI-powered clustering and fact extraction. The system takes multiple news articles about similar topics, clusters them, extracts factual information, and generates neutral, desensationalized articles.

## Features

- **NLP Processing Pipeline**: Text preprocessing with spaCy, semantic embeddings, and clustering algorithms
- **Fact vs Opinion Classification**: Uses NER, sentiment analysis, and rule-based classification
- **AI Article Generation**: Integration with Google Gemini API for neutral article generation
- **RESTful API**: Async FastAPI with background processing and task tracking
- **Scalable Architecture**: Modular design with proper error handling and validation
- **RSS Feed Integration**: Automated news extraction from configurable RSS sources
- **Cluster Management**: Tools for creating, analyzing and maintaining article clusters
- **MongoDB Integration**: Persistent storage for articles, clusters, and processing results

## Tech Stack

- **Backend**: FastAPI (0.115+), Python 3.11+
- **NLP**: spaCy 3.7+, sentence-transformers 3.0+, scikit-learn 1.3+
- **AI**: Google Gemini API
- **Database**: MongoDB via pymongo
- **Web Scraping**: feedparser, beautifulsoup4, requests
- **Processing**: TF-IDF, clustering algorithms, semantic embeddings
- **Environment**: python-dotenv for configuration management

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd infact-platform/backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Configure environment variables**
   ```bash
   # Copy the example .env file and modify as needed
   cp .env.example .env
   ```

6. **Set up environment variables in .env file**
   ```bash
   # MongoDB Configuration
   MONGODB_URI="mongodb+srv://username:password@cluster.mongodb.net/database?retryWrites=true&w=majority"
   MONGODB_DB_NAME="infact_db"
   MONGODB_ARTICLE_COLLECTION="articles"
   MONGODB_CLUSTERS_COLLECTION="clusters"
   MONGODB_FACT_CHECKS_COLLECTION="fact_checks"

   # API Keys
   GEMINI_API_KEY="your_gemini_api_key_here"
   ```

7. **Get Google Gemini API Key**
   - Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Create a new API key
   - Add it to your `.env` file

## Usage

### Starting the Server

```bash
python main.py
```

The API will be available at `http://localhost:8091`

### API Documentation

Visit `http://localhost:8091/docs` for interactive Swagger documentation.

### Basic Usage Example

```python
import requests

# Sample articles for processing
articles = [
    {
        "title": "Former President Arrested on Corruption Charges",
        "content": "Former President was arrested today on charges of misusing state funds...",
        "source": "Daily Mirror",
        "url": "https://example.com/article1"
    },
    {
        "title": "Ex-Leader Faces Legal Action Over Fund Misuse", 
        "content": "Legal proceedings have begun against the former leader for alleged financial misconduct...",
        "source": "The Island",
        "url": "https://example.com/article2"
    }
]

# Process articles with storage
response = requests.post(
    "http://localhost:8091/api/v1/clusters/process-with-storage",
    json={
        "articles": articles,
        "n_clusters": 3,
        "store_clusters": True,
        "merge_similar": True
    }
)

print(response.json())
```

## API Endpoints

### Article Processing
- `POST /articles/sync_process` - Process articles synchronously
- `POST /articles/process` - Process articles asynchronously

### Cluster Storage & Processing  
- `POST /clusters/process-with-storage` - Process articles and store clusters
- `POST /clusters/scrape-process-store` - Complete pipeline from RSS to storage

### Article Management
- `GET /article-management/articles` - List all articles
- `GET /article-management/articles/{article_id}` - Get specific article

### RSS News Extraction
- `POST /news-extraction/extract` - Extract from RSS feeds

## Project Structure

```
backend/
├── main.py                     # FastAPI application entry point
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables (not in repo)
├── .env.example             # Environment template
├── core/                    # Core configuration and database
│   ├── config.py           # Application configuration
│   └── database.py         # MongoDB connection setup
├── routers/                # API route handlers
│   ├── __init__.py        
│   ├── cluster_processing.py    # Article clustering and processing
│   ├── cluster_retrievel.py     # Cluster data retrieval (note: typo in filename)
│   ├── cluster_maintainance.py  # Cluster management operations (note: typo in filename)
│   ├── article_management.py    # Article CRUD operations
│   └── news_extraction.py       # RSS feed extraction
├── schemas/               # Pydantic data models
│   ├── __init__.py       
│   ├── article.py        # Article-related schemas
│   ├── cluster.py        # Clustering schemas
│   ├── cluster_storage.py # Cluster storage schemas
│   ├── rss_feeds.py      # RSS extraction schemas
│   └── response.py       # API response schemas
├── utils/                # Core processing utilities
│   ├── cluster_storage.py      # Cluster storage management
│   ├── cluster_storage_utils.py # Storage utilities
│   ├── image_service.py         # Image processing service
│   ├── data_collection/        # Data collection utilities
│   │   └── rss_extractor.py   # RSS feed processing
│   └── data_processing/       # NLP and AI processing
│       ├── nlp_processor.py   # Main NLP coordinator
│       ├── clustering.py      # Clustering algorithms
│       ├── fact_extractor.py  # Fact extraction
│       └── ai_generator.py    # AI content generation
```

## Processing Pipeline

1. **RSS Extraction**: Automated collection from configured news sources
2. **Text Preprocessing**: Cleaning, tokenization, and normalization
3. **Embedding Generation**: Semantic embeddings using sentence-transformers
4. **Clustering**: Grouping similar articles using clustering algorithms
5. **Fact Extraction**: Separating facts from opinions and musings
6. **AI Generation**: Creating neutral, desensationalized articles
7. **Storage**: Persisting results in MongoDB with cross-references

## Configuration

Configure the application through environment variables in your `.env` file:

```bash
# MongoDB Settings
MONGODB_URI="your_mongodb_connection_string"
MONGODB_DB_NAME="infact_db"

# Collection Names
MONGODB_ARTICLE_COLLECTION="articles"
MONGODB_CLUSTERS_COLLECTION="clusters"
MONGODB_FACT_CHECKS_COLLECTION="fact_checks"

# API Keys
GEMINI_API_KEY="your_gemini_api_key"
```

## Error Handling

The API includes comprehensive error handling:
- Input validation with Pydantic schemas
- MongoDB connection error handling
- API key validation and fallbacks
- Graceful degradation when external services are unavailable
- Detailed error messages and logging

## MongoDB Collections

### Articles Collection
Stores individual news articles with metadata:
```json
{
  "_id": "ObjectId",
  "title": "Article Title",
  "content": "Full article content",
  "source": "News Source",
  "url": "https://...",
  "published_at": "ISO datetime",
  "extracted_at": "ISO datetime",
  "cluster_id": "reference to cluster",
  "image_url": "https://..."
}
```

### Clusters Collection
Stores processed article clusters:
```json
{
  "_id": "ObjectId",
  "name": "Cluster Name",
  "articles": [...], // Full article data
  "facts": [...],
  "musings": [...],
  "generated_article": "AI generated content",
  "factual_summary": "Summary",
  "keywords": [...],
  "sources": [...],
  "created_at": "ISO datetime",
  "updated_at": "ISO datetime"
}
```

## Development

To run in development mode with auto-reload:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8091
```

## Production Deployment

For production deployment:

1. **Configure production environment variables**
2. **Set up proper CORS origins** in `main.py`
3. **Use a production ASGI server**:
   ```bash
   pip install gunicorn
   gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8091
   ```
4. **Set up MongoDB cluster** for production
5. **Configure monitoring and logging**
6. **Set up SSL/TLS certificates**

## Troubleshooting

### Common Issues

1. **MongoDB Connection Error**:
   - Check your `MONGODB_URI` in the `.env` file
   - Ensure MongoDB cluster allows connections from your IP
   - Verify database credentials

2. **spaCy model not found**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

3. **Gemini API errors**:
   - Check your API key in the `.env` file
   - Verify API usage limits and quotas
   - Ensure API key has proper permissions

4. **Missing environment variables**:
   - Copy `.env.example` to `.env`
   - Fill in all required variables

5. **Port already in use**:
   - Change the port in `main.py` from 8091 to another available port
   - Or kill the process using port 8091

### Development Tips

- Use the interactive docs at `http://localhost:8091/docs` for testing endpoints
- Check the MongoDB collections to verify data storage
- Monitor server logs for debugging information
- Use the task tracking endpoints for background operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes following the existing code structure
4. Add appropriate tests
5. Update documentation if needed
6. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Check the API documentation at `http://localhost:8091/docs`
- Review the troubleshooting section above
- Verify your environment configuration
- Check MongoDB connection and data
- Open an issue on GitHub with detailed error information
