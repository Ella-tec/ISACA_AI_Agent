import sqlite3
from app.config import settings

def log_interaction(user_id: str, question: str, answer: str, confidence: float):
    conn = sqlite3.connect(settings.LOG_DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            question TEXT,
            answer TEXT,
            confidence REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        INSERT INTO logs (user_id, question, answer, confidence)
        VALUES (?, ?, ?, ?)
    """, (user_id, question, answer, confidence))

    conn.commit()
    conn.close()
