import json
from typing import List, Dict
from app.config import settings

def load_vector_store() -> List[Dict]:
    try:
        with open(settings.VECTOR_DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_vector_store(data: List[Dict]):
    with open(settings.VECTOR_DB_FILE, "w") as f:
        json.dump(data, f, indent=2)
