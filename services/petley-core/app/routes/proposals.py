from typing import Literal

from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel, Field

from app.services.proposals import (
    ProposalNotFoundError,
    ProposalStateError,
    approve_proposal,
    create_proposal,
    get_proposal,
    list_proposals,
    reject_proposal,
)


router = APIRouter(
    prefix="/memory/proposals",
    tags=["memory proposals"],
)


class ProposalCreateRequest(BaseModel):
    source: str = Field(
        default="user",
        min_length=1,
        max_length=100,
    )
    category: str = Field(
        min_length=1,
        max_length=100,
    )
    target: str = Field(
        min_length=1,
        max_length=500,
    )
    summary: str = Field(
        min_length=1,
        max_length=1000,
    )
    content: dict = Field(default_factory=dict)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
def create_memory_proposal(
    request: ProposalCreateRequest,
) -> dict:
    return create_proposal(
        source=request.source,
        category=request.category,
        target=request.target,
        summary=request.summary,
        content=request.content,
    )


@router.get("")
def get_memory_proposals(
    proposal_status: Literal[
        "pending",
        "approved",
        "rejected",
    ]
    | None = Query(
        default=None,
        alias="status",
    ),
) -> list[dict]:
    return list_proposals(status=proposal_status)


@router.get("/{proposal_id}")
def get_memory_proposal(proposal_id: str) -> dict:
    proposal = get_proposal(proposal_id)

    if proposal is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proposal not found.",
        )

    return proposal


@router.post("/{proposal_id}/approve")
def approve_memory_proposal(proposal_id: str) -> dict:
    try:
        return approve_proposal(proposal_id)

    except ProposalNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proposal not found.",
        )

    except ProposalStateError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )


@router.post("/{proposal_id}/reject")
def reject_memory_proposal(proposal_id: str) -> dict:
    try:
        return reject_proposal(proposal_id)

    except ProposalNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proposal not found.",
        )

    except ProposalStateError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )
