from fastapi import APIRouter

from app.config import APP_NAME, MEMORY_ROOT, VERSION

router = APIRouter(tags=["System"])


@router.get("/health")
def health() -> dict:
    return {
        "status": "healthy",
        "service": APP_NAME,
        "version": VERSION,
        "memory": "online" if MEMORY_ROOT.is_dir() else "unavailable",
    }


@router.get("/version")
def version() -> dict:
    return {
        "service": APP_NAME,
        "version": VERSION,
    }
