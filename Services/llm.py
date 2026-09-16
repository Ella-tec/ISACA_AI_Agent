from openai import OpenAI
from app.config import settings
from app.services.retrieval import RetrievedChunk
from typing import List

client = OpenAI(api_key=settings.OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are the ISACA Chapter Support Agent.

RULES:
- Use ONLY the approved ISACA content provided.
- If the answer is not supported, say “I am not sure.”
- Never invent policies or legal rules.
- Keep answers short, clear, and friendly.
"""

def build_context(chunks: List[RetrievedChunk]) -> str:
    return "\n\n".join([f"[{c.source_id}] {c.text}" for c in chunks])

async def generate_answer(question: str, chunks: List[RetrievedChunk]) -> str:
    context = build_context(chunks)

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
    ]

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.1
    )

    return completion.choices[0].message.content
