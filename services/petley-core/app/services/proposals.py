import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

from app.config import PROPOSALS_ROOT


VALID_STATUSES = {"pending", "approved", "rejected"}


class ProposalNotFoundError(Exception):
    """Raised when a proposal cannot be found."""


class ProposalStateError(Exception):
    """Raised when an invalid proposal status change is requested."""


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def proposal_path(proposal_id: str) -> Path:
    return PROPOSALS_ROOT / f"{proposal_id}.json"


def write_proposal(proposal: dict) -> None:
    """
    Write a proposal atomically.

    The temporary file is fully written before replacing the existing file,
    reducing the risk of leaving a partially written JSON document.
    """
    PROPOSALS_ROOT.mkdir(parents=True, exist_ok=True)

    destination = proposal_path(proposal["id"])
    temporary = destination.with_suffix(".json.tmp")

    temporary.write_text(
        json.dumps(proposal, indent=2) + "\n",
        encoding="utf-8",
    )

    temporary.replace(destination)


def create_proposal(
    source: str,
    category: str,
    target: str,
    summary: str,
    content: dict | None = None,
) -> dict:
    proposal_id = uuid4().hex[:12]

    proposal = {
        "id": proposal_id,
        "status": "pending",
        "created_at": utc_now(),
        "updated_at": None,
        "approved_at": None,
        "rejected_at": None,
        "source": source,
        "category": category,
        "target": target,
        "summary": summary,
        "content": content or {},
    }

    write_proposal(proposal)
    return proposal


def get_proposal(proposal_id: str) -> dict | None:
    path = proposal_path(proposal_id)

    if not path.exists():
        return None

    return json.loads(path.read_text(encoding="utf-8"))


def list_proposals(status: str | None = None) -> list[dict]:
    if not PROPOSALS_ROOT.exists():
        return []

    if status is not None and status not in VALID_STATUSES:
        raise ValueError(f"Invalid proposal status: {status}")

    proposals: list[dict] = []

    for path in PROPOSALS_ROOT.glob("*.json"):
        proposal = json.loads(path.read_text(encoding="utf-8"))

        if status is None or proposal.get("status") == status:
            proposals.append(proposal)

    return sorted(
        proposals,
        key=lambda proposal: proposal.get("created_at", ""),
        reverse=True,
    )


def change_proposal_status(
    proposal_id: str,
    new_status: str,
) -> dict:
    if new_status not in {"approved", "rejected"}:
        raise ValueError(f"Unsupported final status: {new_status}")

    proposal = get_proposal(proposal_id)

    if proposal is None:
        raise ProposalNotFoundError(proposal_id)

    current_status = proposal.get("status")

    if current_status != "pending":
        raise ProposalStateError(
            f"Proposal is already {current_status}."
        )

    changed_at = utc_now()

    proposal["status"] = new_status
    proposal["updated_at"] = changed_at

    if new_status == "approved":
        proposal["approved_at"] = changed_at
    else:
        proposal["rejected_at"] = changed_at

    write_proposal(proposal)
    return proposal


def approve_proposal(proposal_id: str) -> dict:
    return change_proposal_status(
        proposal_id=proposal_id,
        new_status="approved",
    )


def reject_proposal(proposal_id: str) -> dict:
    return change_proposal_status(
        proposal_id=proposal_id,
        new_status="rejected",
    )
