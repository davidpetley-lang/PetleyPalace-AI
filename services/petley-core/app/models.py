from pydantic import BaseModel, Field


class MemorySearchRequest(BaseModel):
    query: str = Field(
        min_length=2,
        max_length=200,
        description="Text to search for in Petley Palace memory",
    )

    category: str | None = Field(
        default=None,
        description="Optional memory category such as projects or profile",
    )

    limit: int = Field(
        default=10,
        ge=1,
        le=50,
        description="Maximum number of results",
    )
