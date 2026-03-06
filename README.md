# 🗞️ InFact Platform - AI-Powered News Desensationalization Engine

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-5.0+-brightgreen.svg)](https://www.mongodb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Transform sensationalized news into factual, neutral reporting through advanced AI and NLP techniques**

A FastAPI-powered news processing and analysis platform that extracts facts from news articles, clusters similar content, and presents desensationalized information. Tired of clickbait headlines and biased spins? InFact cuts through the noise to deliver just the facts—because who has time for drama in their daily news?

Built with **Python FastAPI** for robust API services and advanced AI processing pipelines.

🔗 **[Original InFact Implementation](https://github.com/LazySeaHorse/Infact)**

<img width="1086" height="403" alt="Screenshot 2025-08-31 000610" src="https://github.com/user-attachments/assets/506ed15e-d6b5-408c-95b7-21fea0f96b99" />

<img width="1085" height="600" alt="Screenshot 2025-08-31 000646" src="https://github.com/user-attachments/assets/03ee25b2-cf54-4c4e-bae9-884c7b555b82" />

<img width="1087" height="403" alt="Screenshot 2025-08-31 000659" src="https://github.com/user-attachments/assets/8d3f72f3-38b5-4566-ab2c-004ce7924925" />

<img width="1088" height="570" alt="Screenshot 2025-08-31 001255" src="https://github.com/user-attachments/assets/c347c048-9fbf-4b3a-9558-c12bc029a679" />


<img width="1088" height="414" alt="Screenshot 2025-08-31 000727" src="https://github.com/user-attachments/assets/900f8c0e-30f7-4685-9fd5-8f966edf1ea7" />

---


## 🔍 Overview

InFact is your ultimate shield against sensationalized news! This platform automatically pulls articles from RSS feeds and external APIs, processes them with cutting-edge NLP to separate facts from opinions, clusters similar stories, and generates neutral summaries using AI. Built by a talented team from Sri Lanka, it's perfect for journalists, researchers, or anyone who wants unbiased information without the hype.

### 🏗️ Architecture

This implementation features a **unified FastAPI architecture**:

- **🧠 FastAPI Backend**: Comprehensive API service handling news aggregation, AI processing, clustering, and data management
- **🔄 Integrated Pipeline**: Single service architecture with modular components for scalability

```
📁 InFact Platform/
├── 🧠 backend/                    # FastAPI Backend Service
│   ├── main.py                    # FastAPI application entry
│   ├── core/                      # Configuration & database
│   ├── schemas/                   # Pydantic data models
│   ├── routers/                   # API endpoints & business logic
│   └── utils/                     # NLP & AI processing tools
│
├── 📊 frontend/                   # React Frontend (Optional)
└── 📓 notebook/                   # Research & Development
```

---

## ✨ Key Features

### 🧠 **AI-Powered Processing**
- **Smart Article Clustering** - Groups related news stories using semantic similarity
- **Fact vs Opinion Classification** - Separates factual information from editorial content  
- **Neutral Article Generation** - Creates unbiased summaries using Google Gemini AI
- **Sentiment Analysis** - Identifies and neutralizes emotional language
- **Duplicate Detection** - Automatic duplicate article detection and filtering

### 🔍 **Advanced Analytics**
- **Trending Topic Detection** - Identifies emerging news patterns
- **Source Bias Analysis** - Tracks how different outlets cover the same story
- **Real-time Statistics** - Comprehensive metrics and insights
- **Similarity Scoring** - ML-based content similarity detection
- **Weekly Digests** - Automated news summaries

### 🏗️ **Production Architecture**
- **FastAPI Backend** - High-performance async API with comprehensive routing
- **Background Processing** - Async task handling with progress tracking
- **MongoDB Integration** - Scalable document storage with intelligent clustering
- **Modular Design** - Clean separation of concerns with comprehensive error handling
- **RSS Feed Automation** - Automated news ingestion from configurable sources

### 📊 **Rich Data Management**
- **URL Tracking** - Maintains links to original sources
- **Image Processing** - Automatic image selection for clusters
- **Multi-source Aggregation** - Combines articles from multiple news outlets
- **Historical Analysis** - Tracks news evolution over time
- **Search & Filtering** - Advanced query capabilities

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.11+**
- **MongoDB 5.0+** (local or cloud)
- **Google Gemini API Key** ([Get one here](https://aistudio.google.com/app/apikey))

### 1. Clone & Setup

```bash
# Clone the repository
git clone <repository-url>
cd infact-platform/backend
```

### 2. Install Dependencies

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

### 3. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your configuration
# MongoDB URI, Gemini API key, etc.
```

### 4. Launch Service

```bash
# Start the FastAPI server
python main.py
# Available at: http://localhost:8091
```

---

## 📋 API Documentation

### 🧠 FastAPI Backend Endpoints

Comprehensive news processing and analytics APIs:

#### **Article Processing**
```bash
# Process articles synchronously
curl -X POST "http://localhost:8091/api/v1/articles/sync_process" \
  -H "Content-Type: application/json" \
  -d '{"articles": [...], "n_clusters": 3}'

# Process articles asynchronously
curl -X POST "http://localhost:8091/api/v1/articles/process" \
  -H "Content-Type: application/json" \
  -d '{"articles": [...], "n_clusters": 3}'

# Get processing task status
curl "http://localhost:8091/api/v1/articles/task/{task_id}"
```

#### **Cluster Management**
```bash
# Process and store clusters
curl -X POST "http://localhost:8091/api/v1/clusters/process-with-storage" \
  -H "Content-Type: application/json" \
  -d '{"articles": [...], "n_clusters": 3, "store_clusters": true}'

# Get recent clusters
curl "http://localhost:8091/api/v1/clusters/recent?limit=10"

# Search clusters
curl -X POST "http://localhost:8091/api/v1/clusters/search" \
  -H "Content-Type: application/json" \
  -d '{"query": "climate change", "limit": 10}'

# Get trending topics
curl "http://localhost:8091/api/v1/clusters/trending-topics?days_back=30"

# Auto-processing pipeline
curl -X POST "http://localhost:8091/api/v1/clusters/scrape-process-store?days_back=7"
```

#### **RSS News Extraction**
```bash
# Extract from RSS feeds
curl -X POST "http://localhost:8091/api/v1/news-extraction/extract" \
  -H "Content-Type: application/json" \
  -d '{"from_date": "2025-08-22", "max_articles": 50}'

# Async RSS extraction
curl -X POST "http://localhost:8091/api/v1/news-extraction/extract/async" \
  -H "Content-Type: application/json" \
  -d '{"from_date": "2025-08-22", "max_articles": 50}'

# Get extraction task status
curl "http://localhost:8091/api/v1/news-extraction/task/{task_id}"
```

#### **Article Management**
```bash
# List all articles
curl "http://localhost:8091/api/v1/article-management/articles?limit=20&skip=0"

# Get specific article
curl "http://localhost:8091/api/v1/article-management/articles/{article_id}"

# Delete article
curl -X DELETE "http://localhost:8091/api/v1/article-management/articles/{article_id}"
```

📖 **Full API Documentation:**
- Interactive Docs: `http://localhost:8091/docs` (Swagger UI)
- OpenAPI Schema: `http://localhost:8091/openapi.json`

---

## 🛠️ Tech Stack

### 🧠 **Backend Framework**
- **Framework**: FastAPI (Python 3.11+)
- **NLP & ML**: spaCy, sentence-transformers, scikit-learn, gensim
- **AI**: Google Generative AI (Gemini 2.0 Flash)
- **Data Processing**: NumPy, pandas, PyTorch, NLTK
- **Database**: MongoDB (via pymongo)
- **Features**: Async processing, background tasks, ML pipelines

### 📊 **Data & Processing**
- **Web Scraping**: feedparser, beautifulsoup4, requests
- **Text Processing**: TF-IDF, clustering algorithms, semantic embeddings
- **Image Processing**: Pillow, automatic image selection
- **Environment**: python-dotenv for configuration management

---

## 🔄 Processing Pipeline

```mermaid
graph TD
    A[📰 RSS/API Sources] --> B[🔄 FastAPI Backend]
    B --> C[📝 Article Extraction]
    C --> D[🔤 Text Preprocessing]
    D --> E[🧠 Semantic Embeddings]
    E --> F[🎯 Clustering Algorithm]
    F --> G[🔍 Similarity Check]
    G --> H{📊 Similar Cluster?}
    H -->|Yes| I[🔗 Merge Clusters]
    H -->|No| J[✨ Create New Cluster]
    I --> K[📋 Fact Extraction]
    J --> K
    K --> L[🤖 AI Generation]
    L --> M[💾 Store in MongoDB]
    M --> N[📈 Update Analytics]
    N --> O[🔄 Return Results]
```

### Pipeline Steps

1. **📡 Data Ingestion** - FastAPI fetches from RSS feeds and external APIs
2. **📝 Text Preprocessing** - Tokenization, lemmatization, noise removal
3. **🧠 Embedding Generation** - Semantic vectors using sentence-transformers
4. **🎯 Smart Clustering** - KMeans with TF-IDF enhancement
5. **🔍 Similarity Analysis** - Compare with existing clusters
6. **🔗 Intelligent Merging** - Combine similar clusters or create new ones
7. **📋 Fact Extraction** - NER + sentiment analysis for classification
8. **🔄 Deduplication** - Remove redundant information
9. **🤖 AI Generation** - Create neutral summaries with Gemini
10. **💾 Persistent Storage** - MongoDB with indexing
11. **🖼️ Media Processing** - Image selection and URL tracking

---

## 📁 Project Structure

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
│   ├── cluster_retrievel.py     # Cluster data retrieval
│   ├── cluster_maintainance.py  # Cluster management operations
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

---

## ⚙️ Configuration

Configure the application through environment variables in your `.env` file:

```bash
# MongoDB Settings
MONGODB_URI="mongodb+srv://username:password@cluster.mongodb.net/database?retryWrites=true&w=majority"
MONGODB_DB_NAME="infact_db"

# Collection Names
MONGODB_ARTICLE_COLLECTION="articles"
MONGODB_CLUSTERS_COLLECTION="clusters"
MONGODB_FACT_CHECKS_COLLECTION="fact_checks"

# API Keys
GEMINI_API_KEY="your_gemini_api_key"
```

---

## 🧪 Testing

### Backend Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test files
pytest tests/test_clustering.py
```

### Integration Testing
```bash
# Test complete pipeline
curl -X POST "http://localhost:8091/api/v1/clusters/scrape-process-store?max_articles=5"

# Health check
curl "http://localhost:8091/health"
```

---

## 🚀 Performance Optimization

### FastAPI Backend
- **Async Processing**: Background tasks for heavy operations
- **Connection Pooling**: Efficient MongoDB connections
- **Caching**: Intelligent caching for repeated operations
- **Batch Processing**: GPU acceleration when available

### MongoDB
- **Indexing**: Proper indexing on frequently queried fields
- **Aggregation**: Efficient data aggregation pipelines
- **Sharding**: Horizontal scaling for large datasets

---

## 🔧 Development

### Development Setup
```bash
# Clone and setup
git clone <repository-url>
cd infact-platform/backend

# Setup environment
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt

# Run in development mode
python main.py
```

### Adding New Features
1. **Create router** in `routers/` directory
2. **Define schemas** in `schemas/` directory
3. **Add utilities** in `utils/` directory
4. **Update main.py** to include new router
5. **Add tests** in `tests/` directory

### Contribution Guidelines
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 🐛 Troubleshooting

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

4. **Port already in use**:
   - Change the port in `main.py` from 8091 to another available port
   - Or kill the process using port 8091

### Development Tips
- Use the interactive docs at `http://localhost:8091/docs` for testing endpoints
- Check the MongoDB collections to verify data storage
- Monitor server logs for debugging information
- Use the task tracking endpoints for background operations

---

## 👥 Contributors

This project was built by an awesome team from the **University of Moratuwa, Sri Lanka**:

- **🚀 Backend Architect**: [HimathX](https://github.com/HimathX) (Dhanapalage Himath Nimpura Dhanapala) – FastAPI backend & MongoDB integration
- **🎨 Frontend Wizard**: [codevector-2003](https://github.com/codevector-2003) (Haren Daishika) – React interface & user experience  
- **🧠 AI/ML Engineer**: [LazySeaHorse](https://github.com/LazySeaHorse) (Raj Pankaja) – NLP pipeline & AI processing

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">


*Built with ❤️ (and a bit of caffeine) by the InFact Team. Stay factual, folks!* 🚀

</div>