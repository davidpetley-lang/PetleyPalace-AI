from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

APP_NAME = "Petley Core"
VERSION = "0.1.0"
MEMORY_ROOT = Path("/data/memory")

app = FastAPI(
    title=APP_NAME,
    description="Core API for Petley Palace AI",
    version=VERSION,
)


@app.get("/", include_in_schema=False)
def root() -> RedirectResponse:
    return RedirectResponse(url="/docs")


@app.get("/health", tags=["System"])
def health() -> dict:
    return {
        "status": "healthy",
        "service": APP_NAME,
        "version": VERSION,
        "memory": "online" if MEMORY_ROOT.is_dir() else "unavailable",
    }


@app.get("/version", tags=["System"])
def version() -> dict:
    return {
        "service": APP_NAME,
        "version": VERSION,
    }


@app.get("/memory/categories", tags=["Memory"])
def memory_categories() -> dict:
    if not MEMORY_ROOT.is_dir():
        return {
            "categories": [],
            "count": 0,
            "error": "Memory directory is unavailable",
        }

    categories = sorted(
        item.name
        for item in MEMORY_ROOT.iterdir()
        if item.is_dir() and not item.name.startswith(".")
    )

    return {
        "categories": categories,
        "count": len(categories),
    }


@app.get("/projects", tags=["Memory"])
def projects() -> dict:
    project_directory = MEMORY_ROOT / "projects"

    if not project_directory.is_dir():
        return {
            "projects": [],
            "count": 0,
            "error": "Projects directory is unavailable",
        }

    results = []

    for path in sorted(project_directory.glob("*.md")):
        title = path.stem.replace("-", " ").title()

        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
        except OSError:
            pass

        results.append(
            {
                "id": path.stem,
                "title": title,
                "source": f"projects/{path.name}",
            }
        )

    return {
        "projects": results,
        "count": len(results),
    }
