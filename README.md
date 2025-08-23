# Infact 📰

<div align="center">
  <img src="path/to/infact_banner.png" alt="InFact Banner" width="600">
</div>

A full-stack news processing and analysis platform that extracts facts from news articles, clusters similar content, and presents desensationalized information through a modern web interface. Tired of clickbait headlines and biased spins? InFact cuts through the noise to deliver just the facts—because who has time for drama in their daily news?


## 🔍 Overview

InFact is your ultimate shield against sensationalized news! This platform automatically pulls articles from RSS feeds, processes them with cutting-edge NLP to separate facts from fluff, clusters similar stories, and generates neutral summaries using AI. Built by a talented team from Sri Lanka, it's perfect for journalists, researchers, or anyone who wants unbiased info without the hype.

Inspired by advanced pipelines for desensationalizing news (shoutout to those clickbait-busting Jupyter notebooks!), we've turned it into a full-fledged app with a sleek frontend and robust backend.

For more detailed information about the InFact pipeline and its implementation, visit: https://github.com/LazySeaHorse/Infact

## ✨ Features

### Backend (FastAPI)
- **News Extraction**: Pulls fresh articles from RSS feeds like a pro news hound.
- **NLP Magic**: Preprocesses text with spaCy, generates embeddings, and clusters articles smarter than your average algorithm.
- **Fact Detective**: Spots facts vs. opinions using NER, sentiment analysis, and clever rules.
- **Clustering Wizardry**: Groups articles with KMeans + TF-IDF for that "aha!" moment.
- **AI Writer**: Uses Google Gemini to craft neutral, fact-based articles—no bias, just bliss.
- **RESTful API**: Async endpoints with background tasks because waiting is so last year.
- **MongoDB Storage**: Keeps everything organized and query-ready.

### Frontend (React + Vite)
- **Slick UI**: Responsive design with Tailwind CSS—looks great on your phone or giant monitor.
- **Article Explorer**: Browse, filter, and dive deep into articles.
- **Cluster Viewer**: Interactive clusters with visuals to spot trends.
- **Source Manager**: Track and tweak your news sources.
- **Tabbed Navigation**: Switch views faster than a news cycle.

## 🏗️ Architecture

The core pipeline processes news through six epic stages:
1. **Preprocessing**: Clean, tokenize, and normalize text.
2. **Clustering**: Group similar articles semantically.
3. **Topic Extraction**: Auto-name clusters with LDA topic modeling.
4. **Fact Extraction**: Pull out facts using NER and sentiment checks.
5. **Deduplication**: Merge duplicates to keep things tidy.
6. **Article Generation**: LLM-powered neutral rewrites.

```
InFact Platform/
├── backend/                # FastAPI backend magic
│   ├── core/              # Config and DB connections
│   ├── routers/           # API routes for all features
│   ├── schemas/           # Pydantic models (data validation FTW)
│   ├── services/          # Business logic brains
│   └── utils/             # Tools for data collection & processing
└── frontend/               # React frontend flair
    ├── public/            # Static goodies
    └── src/               # Components and assets
        ├── assets/        # Images and icons
        └── components/    # Reusable UI bits like NewsCard and TopBar
```

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **NLP & ML**: spaCy, sentence-transformers, scikit-learn, gensim, PyTorch, NLTK
- **AI**: Google Generative AI (Gemini 2.5 Flash)
- **Data Crunching**: NumPy, pandas, FuzzyWuzzy
- **News Tools**: feedparser, beautifulsoup4, aiohttp
- **Database**: MongoDB (via pymongo)
- **Server**: Uvicorn

### Frontend
- **Framework**: React 19.1.1
- **Build Tool**: Vite 7.1.2
- **Styling**: Tailwind CSS 4.1.12
- **Linting**: ESLint 9.33.0

Bonus: GPU acceleration with CUDA for speedy embeddings, and LangChain for prompt orchestration.

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- MongoDB 4.4+ (running locally or via cloud)
- A sense of humor (optional but recommended)

### Backend Setup
1. Jump into backend:
   ```
   cd backend
   ```
2. Virtual env vibes:
   ```
   python -m venv .venv
   source .venv/bin/activate  # Or .\.venv\Scripts\Activate.ps1 on Windows
   ```
3. Install the goods:
   ```
   pip install -r requirements.txt
   ```
4. Install spaCy model:
   ```
   pip install spacy
   python -m spacy download en_core_web_sm
   ```
5. Set env vars (create .env file):
   ```
   MONGODB_URI=mongodb://localhost:27017/infact
   GOOGLE_API_KEY=your_gemini_key_here
   ```
6. Fire it up:
   ```
   python main.py
   ```
   API at `http://localhost:8091`

### Frontend Setup
1. Switch to frontend:
   ```
   cd frontend
   ```
2. Install deps:
   ```
   npm install
   ```
3. Launch dev server:
   ```
   npm run dev
   ```
   App at `http://localhost:5173`

## 📊 Usage

- **Extract News**: Hit the API to pull from RSS feeds.
- **Process Articles**: Send them through the pipeline for clustering and fact extraction.
- **Browse Frontend**: Filter articles, explore clusters, and enjoy desensationalized summaries.
- Test with our demo data—full of over-the-top clickbait to show off the magic!

## 📚 API Documentation

Swagger docs at `http://localhost:8091/docs`. Highlights:
- `/articles/process`: Run the full pipeline.
- `/clusters/create`: Make new clusters.
- `/news/extract`: Grab fresh news.

## 📁 Project Structure

See the Architecture section above for the deets!

## 🧪 Development

Backend reload: `uvicorn main:app --reload --port 8091`  
Frontend: `npm run dev`  
Tests: `pytest` (backend) or `npm run test` (frontend)

## ⚠️ Troubleshooting

- **spaCy Not Found?** Install it with:
  ```
  pip install spacy
  python -m spacy download en_core_web_sm
  ```
- **Model Missing?** Run the above commands again.
- **Memory Woes?** Lower batch sizes or disable CUDA.
- **DB Issues?** Check your MongoDB URI.
- **Frontend Glitches?** Ensure Node version matches.

## 👥 Contributors

This project was built by an awesome team from the University of Moratuwa, Sri Lanka:
- **Backend Mastermind**: [HimathX (Dhanapalage Himath Nimpura Dhanapala)](https://github.com/HimathX) – Handling the heavy lifting with FastAPI and MongoDB.
- **Frontend Wizard**: [codevector-2003 (Haren Daishika)](https://github.com/codevector-2003) – Crafting the beautiful React interface.
- **Pipeline & UI/UX Guru**: [LazySeaHorse (Raj Pankaja)](https://github.com/LazySeaHorse) – Building the core NLP pipeline and UX flow.

Fun fact: We're all passionate about tech, from full-stack dev to AI/ML. Let's collaborate!

## 👥 Contributing

Fork it, branch it, commit it, PR it! We love improvements like multi-language support or real-time features.

## 📄 License

MIT License – Free as in speech (and beer?).

---

Built with ❤️ (and a bit of caffeine) by the InFact Team. Stay factual, folks! 🚀
