import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from app.config import PROPOSALS_ROOT


def create_proposal(
    source: str,
    category: str,
    target: str,
    summary: str,
    content: dict | None = None,
) -> dict:
    PROPOSALS_ROOT.mkdir(parents=True, exist_ok=True)

    proposal_id = uuid4().hex[:12]

    proposal = {
        "id": proposal_id,
        "status": "pending",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "category": category,
        "target": target,
        "summary": summary,
        "content": content or {},
    }

    proposal_path = PROPOSALS_ROOT / f"{proposal_id}.json"

    proposal_path.write_text(
        json.dumps(proposal, indent=2),
        encoding="utf-8",
    )

    return proposal


def list_proposals() -> list[dict]:
    if not PROPOSALS_ROOT.exists():
        return []

    proposals = []

    for proposal_path in sorted(PROPOSALS_ROOT.glob("*.json")):
        proposals.append(
            json.loads(proposal_path.read_text(encoding="utf-8"))
        )

    return proposals


def get_proposal(proposal_id: str) -> dict | None:
    proposal_path = PROPOSALS_ROOT / f"{proposal_id}.json"

    if not proposal_path.exists():
        return None

    return json.loads(proposal_path.read_text(encoding="utf-8"))
