from pydantic import BaseModel, Field


class MediaGetSchema(BaseModel):
    id: str = Field(..., description="Media ID", examples=["123e4567-e89b-12d3-a456-426614174000"])
    title: str = Field(..., description="Media Title", examples=["Amazing movie"])
    type_: str = Field(..., description="Media Type", examples=["movie"])
    size: int = Field(..., description="Media Size", examples=[120])
    duration: int = Field(..., description="Media Duration", examples=[120])
    resolution: str = Field(..., description="Media Resolution", examples=["1080p"])
    path: str = Field(..., description="Media Path", examples=["/path/to/media"])


class MediaCreateSchema(BaseModel):
    title: str = Field(..., description="Media Title", examples=["Amazing movie"])
    type_: str = Field(..., description="Media Type", examples=["movie"])
    size: int = Field(..., description="Media Size", examples=[120])
    duration: int = Field(..., description="Media Duration", examples=[120])
    resolution: str = Field(..., description="Media Resolution", examples=["1080p"])


class MediaUpdateSchema(BaseModel):
    title: str = Field(None, description="Media Title", examples=["Amazing movie"])
    type_: str = Field(None, description="Media Type", examples=["movie"])
    size: int = Field(None, description="Media Size", examples=[120])
    duration: int = Field(None, description="Media Duration", examples=[120])
    resolution: str = Field(None, description="Media Resolution", examples=["1080p"])


class MediaPaginatedResponseSchema(BaseModel):
    page_size: int | None = Field(None, description="Number of items per page", examples=[1])
    page_number: int | None = Field(None, description="Current page number", examples=[1])
    total_pages: int | None = Field(None, description="Total number of pages", examples=[1])
    items: list[MediaGetSchema] = Field(..., description="List of Media")
