from pydantic import BaseModel, Field


class MovieGetSchema(BaseModel):
    id: str = Field(..., description="Movie ID", examples=["123e4567-e89b-12d3-a456-426614174000"])
    title: str = Field(..., description="Movie Title", examples=["Amazing movie"])
    metadata_: dict = Field(..., description="Movie Metadata", examples=[{"duration": 120}])


class MovieCreateSchema(BaseModel):
    title: str = Field(..., description="Movie Title", examples=["Amazing movie"])
    metadata_: dict = Field(..., description="Movie Metadata", examples=[{"duration": 120}])


class MovieUpdateSchema(BaseModel):
    title: str = Field(..., description="Movie Title", examples=["Amazing movie"])
    metadata_: dict = Field(..., description="Movie Metadata", examples=[{"duration": 120}])


class MoviePaginatedResponseSchema(BaseModel):
    page_size: int | None = Field(None, description="Number of items per page", examples=[1])
    page_number: int | None = Field(None, description="Current page number", examples=[1])
    total_pages: int | None = Field(None, description="Total number of pages", examples=[1])
    items: list[MovieGetSchema] = Field(..., description="List of Movies")
