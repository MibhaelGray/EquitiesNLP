import os
import praw
from dotenv import load_dotenv
from datetime import datetime
import sqlite3


load_dotenv()



reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent='script:NgcSZoaaq2yALRUgvvZGLA:1.0 (by /u/Mgray-)'  # Change this to your app name
)

# Access the wallstreetbets subreddit
wsb = reddit.subreddit('wallstreetbets')

# Example 1: Get the 10 hottest posts
print("=== Top 10 Hot Posts ===")
for post in wsb.hot(limit=10):
    print(f"Title: {post.title}")
    print(f"Score: {post.score}")
    print(f"Comments: {post.num_comments}")
    print(f"URL: {post.url}")
    print("-" * 50)




print("Fetching top 1000 posts from r/wallstreetbets (past month)...")
print("=" * 60)

posts_data = []
for post in wsb.top(time_filter='month', limit=100):
    posts_data.append({
        'title': post.title,
        'score': post.score,
        'author': str(post.author) if post.author else '[deleted]',
        'created_utc': post.created_utc,
        'created_date': datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
        'num_comments': post.num_comments,
        'selftext': post.selftext,
        'url': post.url,
        'id': post.id
    })
    
    # Print progress every 100 posts
    if len(posts_data) % 100 == 0:
        print(f"Fetched {len(posts_data)} posts...")

print(f"\nSuccessfully fetched {len(posts_data)} posts!")
print(f"Date range: {posts_data[-1]['created_date']} to {posts_data[0]['created_date']}")
print(f"Top post: '{posts_data[0]['title']}' (Score: {posts_data[0]['score']})")

print(posts_data)