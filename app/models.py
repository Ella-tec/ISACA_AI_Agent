from pydantic import BaseModel
from typing import Optional, List

class ChatRequest(BaseModel):
    user_id: str
    role: str
    question: str

class ChatResponse(BaseModel):
    answer: str
    confidence: float
    grounded: bool
    escalation_required: bool
    escalation_reason: Optional[str] = None
    sources: List[str]
