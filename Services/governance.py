from typing import List
from app.services.retrieval import RetrievedChunk

def estimate_confidence(chunks: List[RetrievedChunk]) -> float:
    if not chunks:
        return 0.0
    return max(c.score for c in chunks)

def should_escalate(confidence: float, answer: str) -> tuple[bool, str | None]:
    if confidence < 0.5:
        return True, "Low grounding confidence"
    if "I am not sure" in answer:
        return True, "LLM uncertainty"
    if "contact Chapter Experience" in answer:
        return True, "Human support required"
    return False, None
