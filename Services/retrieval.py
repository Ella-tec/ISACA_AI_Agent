from typing import List
from app.database.vector_store import load_vector_store

class RetrievedChunk:
    def __init__(self, text: str, source_id: str, score: float):
        self.text = text
        self.source_id = source_id
        self.score = score

async def retrieve_approved_content(query: str) -> List[RetrievedChunk]:
    db = load_vector_store()
    results = []

    for item in db:
        if query.lower() in item["text"].lower():
            results.append(
                RetrievedChunk(
                    text=item["text"],
                    source_id=item["title"],
                    score=0.9
                )
            )

    return results
