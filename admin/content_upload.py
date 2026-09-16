from fastapi import APIRouter, HTTPException
from app.utils.permissions import can_access_admin
from app.database.vector_store import load_vector_store, save_vector_store

router = APIRouter()

@router.post("/admin/upload")
def upload_content(role: str, title: str, text: str):
    if not can_access_admin(role):
        raise HTTPException(status_code=403, detail="Not authorized")

    db = load_vector_store()
    db.append({"title": title, "text": text})
    save_vector_store(db)

    return {"status": "success", "message": "Content uploaded"}
