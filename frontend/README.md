# InFact Platform (Frontend)

A modern React-based frontend for the InFact Platform, providing a user-friendly interface to interact with the article management, clustering, and news extraction services.


## Features

- **Modern UI**: Clean, responsive interface built with React 19 and Tailwind CSS 4
- **Article Management**: View, filter, and organize articles
- **Interactive Clusters**: Explore article clusters with visual representations
- **Source Tracking**: Track and manage news sources
- **Tabbed Interface**: Navigate between different views and features
- **Responsive Design**: Works seamlessly across desktop and mobile devices

## Tech Stack

- **Framework**: React 19.1.1
- **Build Tool**: Vite 7.1.2
- **Styling**: Tailwind CSS 4.1.12
- **Code Quality**: ESLint 9.33.0
- **Component Structure**:
  - ArticleView - Detailed article display
  - Feed - Main news feed display
  - FeedSidebar - Navigation and filtering
  - NewsCard - Article card component
  - SourcesList - News source management
  - TopBar - Main navigation
  
## Getting Started

1. Install dependencies:
   ```
   npm install
   ```

2. Start development server:
   ```
   npm run dev
   ```

3. Build for production:
   ```
   npm run build
   ```

4. Preview production build:
   ```
   npm run preview
   ```

## Development

This project leverages the latest React features and follows modern best practices. The codebase is organized into reusable components with a focus on maintainability and performance.

### Project Structure

```
frontend/
├── index.html              # HTML entry point
├── vite.config.js          # Vite configuration
├── package.json            # Node dependencies
├── public/                 # Static assets
└── src/                    # Source code
    ├── App.jsx             # Main application component
    ├── main.jsx            # React entry point
    ├── assets/             # Images and static resources
    └── components/         # React components
```
