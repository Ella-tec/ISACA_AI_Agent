import sqlite3
from typing import List, Dict
from app.config import settings

def get_connection():
    return sqlite3.connect(settings.LOG_DB_PATH)

def list_logs() -> List[Dict]:
    conn = get_connection()
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

    cur.execute("SELECT id, user_id, question, answer, confidence, timestamp FROM logs")
    rows = cur.fetchall()
    conn.close()

    logs = []
    for r in rows:
        logs.append({
            "id": r[0],
            "user_id": r[1],
            "question": r[2],
            "answer": r[3],
            "confidence": r[4],
            "timestamp": r[5]
        })

    return logs

def get_logs_by_user(user_id: str) -> List[Dict]:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT id, user_id, question, answer, confidence, timestamp
        FROM logs
        WHERE user_id = ?
    """, (user_id,))

    rows = cur.fetchall()
    conn.close()

    logs = []
    for r in rows:
        logs.append({
            "id": r[0],
            "user_id": r[1],
            "question": r[2],
            "answer": r[3],
            "confidence": r[4],
            "timestamp": r[5]
        })

    return logs

def delete_log(log_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM logs WHERE id = ?", (log_id,))
    conn.commit()
    deleted = cur.rowcount > 0
    conn.close()

    return deleted
