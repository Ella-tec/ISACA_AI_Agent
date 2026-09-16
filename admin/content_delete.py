from fastapi import APIRouter, HTTPException
from app.utils.permissions import can_access_admin
from app.database.vector_store import load_vector_store, save_vector_store

router = APIRouter()

@router.delete("/admin/delete")
def delete_content(role: str, title: str):
    if not can_access_admin(role):
        raise HTTPException(status_code=403, detail="Not authorized")

    db = load_vector_store()
    new_db = [item for item in db if item["title"] != title]

    if len(new_db) == len(db):
        raise HTTPException(status_code=404, detail="Content not found")

    save_vector_store(new_db)

    return {"status": "success", "message": f"Deleted content: {title}"}
