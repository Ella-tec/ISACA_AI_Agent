from fastapi import APIRouter, HTTPException
from app.utils.permissions import can_access_admin
from app.database.vector_store import load_vector_store

router = APIRouter()

@router.get("/admin/content")
def list_content(role: str):
    if not can_access_admin(role):
        raise HTTPException(status_code=403, detail="Not authorized")

    return load_vector_store()
