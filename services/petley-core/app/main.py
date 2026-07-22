from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.config import APP_DESCRIPTION, APP_NAME, VERSION
from app.routes.memory import router as memory_router
from app.routes.projects import router as projects_router
from app.routes.system import router as system_router
from app.routes.proposals import router as proposals_router

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=VERSION,
)

app.include_router(system_router)
app.include_router(memory_router)
app.include_router(projects_router)
app.include_router(proposals_router)


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")
