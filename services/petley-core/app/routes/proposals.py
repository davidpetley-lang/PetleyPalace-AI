from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.services.proposals import (
    create_proposal,
    get_proposal,
    list_proposals,
)

router = APIRouter(
    prefix="/memory/proposals",
    tags=["memory proposals"],
)


class ProposalCreateRequest(BaseModel):
    source: str = Field(default="user")
    category: str
    target: str
    summary: str
    content: dict = Field(default_factory=dict)


@router.post("")
def create_memory_proposal(request: ProposalCreateRequest) -> dict:
    return create_proposal(
        source=request.source,
        category=request.category,
        target=request.target,
        summary=request.summary,
        content=request.content,
    )


@router.get("")
def get_memory_proposals() -> list[dict]:
    return list_proposals()


@router.get("/{proposal_id}")
def get_memory_proposal(proposal_id: str) -> dict:
    proposal = get_proposal(proposal_id)

    if proposal is None:
        raise HTTPException(
            status_code=404,
            detail="Proposal not found",
        )

    return proposal
