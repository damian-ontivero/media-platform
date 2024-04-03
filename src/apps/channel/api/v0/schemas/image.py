from pydantic import BaseModel, Field


class ImageSchema(BaseModel):
    path: str = Field(..., description="Image Path", examples=["picture.jpg"])
