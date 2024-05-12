from pydantic import BaseModel, Field


class ContentGetSchema(BaseModel):
    id: str = Field(..., description="Content ID", examples=["123e4567-e89b-12d3-a456-426614174000"])
    files: list[dict] = Field(
        ..., description="Files", examples=[[{"name": "file", "path": "file.mp4", "media_type": "video/mp4"}]]
    )
    rating: float = Field(..., description="Rating", examples=[4.5])
    metadata_: dict = Field(..., description="Metadata", examples=[{"title": "Amazing movie"}])
    channel_id: str = Field(..., description="Channel ID", examples=["123e4567-e89b-12d3-a456-426614174000"])


class ContentCreateSchema(BaseModel):
    rating: float = Field(..., description="Rating", examples=[4.5])
    metadata_: str = Field(..., description="Metadata", examples=['{"title": "Amazing movie"}'])
    channel_id: str = Field(..., description="Channel ID", examples=["123e4567-e89b-12d3-a456-426614174000"])


class ContentUpdateSchema(BaseModel):
    rating: float = Field(..., description="Rating", examples=[4.5])
    metadata_: dict = Field(..., description="Metadata", examples=['{"title": "Amazing movie"}'])
    channel_id: str = Field(..., description="Channel ID", examples=["123e4567-e89b-12d3-a456-426614174000"])


class ContentPaginatedResponseSchema(BaseModel):
    page_size: int | None = Field(None, description="Number of items per page", examples=[1])
    page_number: int | None = Field(None, description="Current page number", examples=[1])
    total_pages: int | None = Field(None, description="Total number of pages", examples=[1])
    items: list[ContentGetSchema] = Field(..., description="List of content items")
