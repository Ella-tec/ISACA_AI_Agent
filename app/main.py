from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

from app.services.chat import handle_chat

app = FastAPI(title="ISACA Chapter Support Agent")

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

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    return await handle_chat(req)
