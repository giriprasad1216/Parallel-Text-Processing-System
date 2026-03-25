# database.py

import sqlite3

def create_table():

    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sentiments (
        review TEXT,
        sentiment TEXT,
        score INTEGER,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_results(results):

    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.executemany(
        "INSERT INTO sentiments (review, sentiment, score, timestamp) VALUES (?, ?, ?, ?)",
        results
    )

    conn.commit()
    conn.close()


def create_index():

    conn = sqlite3.connect("results.db")
    cursor = conn.cursor()

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_sentiment ON sentiments(sentiment)")

    conn.commit()
    conn.close()