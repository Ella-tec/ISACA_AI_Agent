import os

class Settings:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LOG_DB_PATH = "data/logs.db"
    VECTOR_DB_FILE = "data/vector_store.json"
    ESCALATION_EMAIL = "chapterexperience@isaca.org"

settings = Settings()
