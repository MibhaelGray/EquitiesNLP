"""
Simple SQLite Database Setup
Location: src/database.py
"""

import sqlite3
import os

# Connect to database
conn = sqlite3.connect('EquitiesNLP/data/reddit_posts.db')
cursor = conn.cursor()

# Create posts table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        score INTEGER,
        author TEXT,
        created_utc INTEGER,
        created_date TEXT,
        num_comments INTEGER,
        selftext TEXT,  -- Truncated to 500 chars when inserting
        url TEXT
    )
""")

conn.commit()
conn.close()

print("Database created successfully at data/reddit_posts.db")