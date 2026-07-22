from pathlib import Path

from app.config import MEMORY_ROOT, SEARCHABLE_EXTENSIONS


def extract_title(path: Path, content: str) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    return path.stem.replace("-", " ").replace("_", " ").title()


def create_snippet(content: str, query: str, length: int = 240) -> str:
    position = content.lower().find(query.lower())

    if position == -1:
        return content[:length].strip()

    start = max(0, position - 80)
    end = min(len(content), position + len(query) + 160)

    snippet = content[start:end].strip().replace("\n", " ")

    if start > 0:
        snippet = f"...{snippet}"

    if end < len(content):
        snippet = f"{snippet}..."

    return snippet


def list_categories() -> dict:
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


def search_memory_files(
    query: str,
    category: str | None = None,
    limit: int = 10,
) -> dict:
    if not MEMORY_ROOT.is_dir():
        return {
            "query": query,
            "matches": [],
            "count": 0,
            "error": "Memory directory is unavailable",
        }

    search_root = MEMORY_ROOT
    requested_category = None

    if category:
        requested_category = category.strip().lower()
        category_path = MEMORY_ROOT / requested_category

        if not category_path.is_dir():
            return {
                "query": query,
                "category": requested_category,
                "matches": [],
                "count": 0,
                "error": "Memory category does not exist",
            }

        search_root = category_path

    query_lower = query.lower()
    matches = []

    for path in search_root.rglob("*"):
        if not path.is_file():
            continue

        if path.suffix.lower() not in SEARCHABLE_EXTENSIONS:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        score = content.lower().count(query_lower)

        if score == 0:
            continue

        relative_path = path.relative_to(MEMORY_ROOT)

        matches.append(
            {
                "title": extract_title(path, content),
                "category": (
                    relative_path.parts[0]
                    if len(relative_path.parts) > 1
                    else "root"
                ),
                "file": str(relative_path),
                "score": score,
                "snippet": create_snippet(content, query),
            }
        )

    matches.sort(
        key=lambda result: (
            -result["score"],
            result["title"].lower(),
        )
    )

    limited_matches = matches[:limit]

    return {
        "query": query,
        "category": requested_category,
        "matches": limited_matches,
        "count": len(limited_matches),
        "total_matches": len(matches),
    }


def list_projects() -> dict:
    project_directory = MEMORY_ROOT / "projects"

    if not project_directory.is_dir():
        return {
            "projects": [],
            "count": 0,
            "error": "Projects directory is unavailable",
        }

    projects = []

    for path in sorted(project_directory.glob("*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        projects.append(
            {
                "id": path.stem,
                "title": extract_title(path, content),
                "source": f"projects/{path.name}",
            }
        )

    return {
        "projects": projects,
        "count": len(projects),
    }
