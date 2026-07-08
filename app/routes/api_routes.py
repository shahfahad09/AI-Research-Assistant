from fastapi import APIRouter

from app.services.vector_store_service import count_documents

router = APIRouter(prefix="/api")


@router.get("/health")
async def health_check():
    return {
        "status": "running",
        "message": "AI Research Assistant API is working"
    }


@router.get("/stats")
async def stats():
    return {
        "stored_chunks": count_documents()
    }