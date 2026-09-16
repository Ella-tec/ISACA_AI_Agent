from app.utils.sanitizer import sanitize_question
from app.services.retrieval import retrieve_approved_content
from app.services.llm import generate_answer
from app.services.governance import estimate_confidence, should_escalate
from app.services.escalation import escalate_to_staff
from app.utils.logger import log_interaction
from app.models import ChatRequest, ChatResponse

async def handle_chat(req: ChatRequest) -> ChatResponse:
    question = sanitize_question(req.question)

    chunks = await retrieve_approved_content(question)
    confidence = estimate_confidence(chunks)

    if not chunks:
        answer = "I cannot find approved ISACA guidance for this question."
        escalate_to_staff(question, "No approved content")
        return ChatResponse(
            answer=answer,
            confidence=confidence,
            grounded=False,
            escalation_required=True,
            escalation_reason="No approved content",
            sources=[]
        )

    answer = await generate_answer(question, chunks)
    escalation_required, reason = should_escalate(confidence, answer)

    if escalation_required:
        escalate_to_staff(question, reason)

    log_interaction(req.user_id, question, answer, confidence)

    return ChatResponse(
        answer=answer,
        confidence=confidence,
        grounded=True,
        escalation_required=escalation_required,
        escalation_reason=reason,
        sources=[c.source_id for c in chunks]
    )
