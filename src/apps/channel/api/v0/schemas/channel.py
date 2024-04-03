from pydantic import BaseModel, Field

from .image import ImageSchema


class ChannelGetSchema(BaseModel):
    id: str = Field(
        ...,
        description="Channel ID",
        examples=["123e4567-e89b-12d3-a456-426614174000"],
    )
    title: str = Field(
        ..., description="Channel Title", examples=["Channel Title"]
    )
    languages: list[str] = Field(
        ..., description="Languages", examples=[["en", "es"]]
    )
    picture: ImageSchema = Field(
        ..., description="Picture", examples=[{"path": "picture.jpg"}]
    )


class ChannelCreateSchema(BaseModel):
    title: str = Field(
        ..., description="Channel Title", examples=["Channel Title"]
    )
    languages: list[str] = Field(
        ..., description="Languages", examples=[["en", "es"]]
    )
    picture: ImageSchema = Field(
        ..., description="Picture", examples=[{"path": "picture.jpg"}]
    )


class ChannelUpdateSchema(BaseModel):
    title: str = Field(
        ..., description="Channel Title", examples=["Channel Title"]
    )
    languages: list[str] = Field(
        ..., description="Languages", examples=[["en", "es"]]
    )
    picture: ImageSchema = Field(
        ..., description="Picture", examples=[{"path": "picture.jpg"}]
    )


class ChannelPaginatedResponseSchema(BaseModel):
    page_size: int | None = Field(
        None, description="Number of items per page", examples=[1]
    )
    page_number: int | None = Field(
        None, description="Current page number", examples=[1]
    )
    total_pages: int | None = Field(
        None, description="Total number of pages", examples=[1]
    )
    items: list[ChannelGetSchema] = Field(..., description="List of channels")
