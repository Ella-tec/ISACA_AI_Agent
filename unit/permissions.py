def can_access_admin(role: str) -> bool:
    return role in ["isaca_staff", "chapter_experience"]
