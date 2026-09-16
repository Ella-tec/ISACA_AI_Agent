from app.config import settings

def escalate_to_staff(question: str, reason: str):
    # Placeholder: integrate email or ticketing later
    print(f"[ESCALATION] Reason: {reason}")
    print(f"Forwarding to: {settings.ESCALATION_EMAIL}")
    print(f"Question: {question}")
