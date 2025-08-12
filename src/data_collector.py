"""
Data Collector with Simple Database Storage
Location: src/data_collector.py
"""

import os
import praw
from dotenv import load_dotenv
from datetime import datetime
import sqlite3

load_dotenv()

# Reddit connection
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent='script:NgcSZoaaq2yALRUgvvZGLA:1.0 (by /u/Mgray-)'
)

# Get subreddit
wsb = reddit.subreddit('wallstreetbets')

# Collect posts
print("Fetching top posts from r/wallstreetbets...")
posts_data = []
for post in wsb.top(time_filter='month', limit=100):
    posts_data.append({
        'title': post.title,
        'score': post.score,
        'author': str(post.author) if post.author else '[deleted]',
        'created_utc': post.created_utc,
        'created_date': datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
        'num_comments': post.num_comments,
        'selftext': post.selftext[:500] if post.selftext else '',  # Truncate to 500 chars
        'url': post.url,
        'id': post.id
    })

print(f"Collected {len(posts_data)} posts")

# Store in database
conn = sqlite3.connect('../data/reddit_posts.db')
cursor = conn.cursor()

for post in posts_data:
    cursor.execute("""
        INSERT OR REPLACE INTO posts 
        (id, title, score, author, created_utc, created_date, num_comments, selftext, url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        post['id'],
        post['title'],
        post['score'],
        post['author'],
        post['created_utc'],
        post['created_date'],
        post['num_comments'],
        post['selftext'],
        post['url']
    ))

conn.commit()
conn.close()

print("Posts saved to database!")

