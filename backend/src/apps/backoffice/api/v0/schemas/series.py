from pydantic import BaseModel, Field


class SerieReadSchema(BaseModel):
    id: str = Field(..., description="Serie ID", examples=["123e4567-e89b-12d3-a456-426614174000"])
    title: str = Field(..., description="Serie Title", examples=["Amazing movie"])
    type_: str = Field(..., description="Serie Type", examples=["movie"])
    size: int = Field(..., description="Serie Size", examples=[120])
    duration: int = Field(..., description="Serie Duration", examples=[120])
    resolution: str = Field(..., description="Serie Resolution", examples=["1080p"])
    path: str = Field(..., description="Serie Path", examples=["/path/to/media"])


class SerieWriteSchema(BaseModel):
    title: str = Field(..., description="Serie Title", examples=["Amazing movie"])
    type_: str = Field(..., description="Serie Type", examples=["movie"])
    size: int = Field(..., description="Serie Size", examples=[120])
    duration: int = Field(..., description="Serie Duration", examples=[120])
    resolution: str = Field(..., description="Serie Resolution", examples=["1080p"])
    path: str = Field(..., description="Serie Path", examples=["/path/to/media"])


class SeriePaginatedResponseSchema(BaseModel):
    page_size: int | None = Field(None, description="Number of items per page", examples=[1])
    page_number: int | None = Field(None, description="Current page number", examples=[1])
    total_pages: int | None = Field(None, description="Total number of pages", examples=[1])
    items: list[SerieReadSchema] = Field(..., description="List of Serie")
