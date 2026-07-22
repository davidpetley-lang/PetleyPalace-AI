from fastapi import APIRouter

from app.models import MemorySearchRequest
from app.services.memory import list_categories, search_memory_files

router = APIRouter(prefix="/memory", tags=["Memory"])


@router.get("/categories")
def memory_categories() -> dict:
    return list_categories()


@router.post("/search")
def search_memory(request: MemorySearchRequest) -> dict:
    return search_memory_files(
        query=request.query,
        category=request.category,
        limit=request.limit,
    )
