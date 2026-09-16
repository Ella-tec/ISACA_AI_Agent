def sanitize_question(text: str) -> str:
    text = text.strip()
    text = text.replace("\n", " ")
    return text
