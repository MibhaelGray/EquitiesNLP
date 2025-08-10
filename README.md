Reddit Stock Sentiment Dashboard
Core Concept: A live dashboard that monitors and displays sentiment analysis of stock discussions across major Reddit investing forums (r/wallstreetbets, r/stocks, r/investing, etc.)
How it Works:

Collects posts and comments from Reddit via API
Analyzes sentiment using NLP models (like FinBERT) to rate discussions as bullish/bearish
Aggregates sentiment scores by ticker symbol over rolling time windows
Displays real-time sentiment trends, mention volumes, and confidence metrics on a web dashboard

Key Features:

Tracks top 50-100 most-mentioned stocks
Calculates rolling sentiment averages (e.g., 7-day windows)
Filters out bots, spam, and low-quality content
Shows sentiment variance (agreement vs. disagreement levels)
Weights different subreddits based on quality/reliability

Primary Value:

Identifies emerging retail investor trends
Provides risk monitoring through sentiment extremes
Serves as a market sentiment gauge and educational tool

Technical Stack: Python (PRAW for Reddit API, FinBERT for sentiment), time-series database, web framework with WebSocket support for real-time updates
Note: Designed as a sentiment monitoring tool and learning project, not as a predictive trading system.