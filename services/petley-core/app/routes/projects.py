from fastapi import APIRouter

from app.services.memory import list_projects

router = APIRouter(tags=["Projects"])


@router.get("/projects")
def projects() -> dict:
    return list_projects()
