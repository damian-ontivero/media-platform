from fastapi import APIRouter, Body, File, Header, Path, Query, UploadFile, status
from typing_extensions import Annotated

from ..controllers.media import (
    MediaDeleteController,
    MediaFileGetController,
    MediaGetController,
    MediaPostController,
    MediaPutController,
    MediasGetController,
)
from ..dependecy_injection import container
from ..schemas import MediaPaginatedResponseSchema, MediaReadSchema, MediaWriteSchema

router = APIRouter(prefix="/media", tags=["Media"])


@router.get("", response_model=MediaPaginatedResponseSchema, status_code=status.HTTP_200_OK, description="Search Media")
async def search(
    criteria: Annotated[
        str,
        Query(
            ...,
            description="""
    The criteria must be a base64 encoded *INLINE* JSON string with the following structure:
    
    {
        "filter": {
        "conjunction": "AND",
        "conditions": [
            {
                "field": "channel_id",
                "operator": "CONTAINS",
                "value": "1"
            }
            ]
        },
        "sort": [
            {
            "field": "rating",
            "direction": "ASC"
            }
        ],
        "page_size": 15,
        "page_number": 1
    }

            """,
            example="eyJmaWx0ZXIiOnsiY29uanVuY3Rpb24iOiJBTkQiLCJjb25kaXRpb25zIjpbeyJmaWVsZCI6ImNoYW5uZWxfaWQiLCJvcGVyYXRvciI6IkNPTlRBSU5TIiwidmFsdWUiOiIxIn1dfSwic29ydCI6W3siZmllbGQiOiJyYXRpbmciLCJkaXJlY3Rpb24iOiJBU0MifV0sInBhZ2Vfc2l6ZSI6MTUsInBhZ2VfbnVtYmVyIjoxfQ==",
        ),
    ] = None
):
    controller: MediasGetController = container.get("MediasGetController")
    return await controller.run(criteria)


@router.get("/{id}", response_model=MediaReadSchema, status_code=status.HTTP_200_OK, description="Find Media")
async def find(
    id: Annotated[str, Path(..., description="Id of the Media", example="123e4567-e89b-12d3-a456-426614174000")]
):
    controller: MediaGetController = container.get("MediaGetController")
    return await controller.run(id)


@router.post("", status_code=status.HTTP_201_CREATED, description="Create Media")
async def create(media: MediaWriteSchema = Body(...), file: UploadFile = File(...)):
    controller: MediaPostController = container.get("MediaPostController")
    return await controller.run(media, file)


@router.put("/{id}", status_code=status.HTTP_200_OK, description="Update Media")
async def update(
    id: Annotated[str, Path(..., description="Id of the Media", example="123e4567-e89b-12d3-a456-426614174000")],
    media: MediaWriteSchema = Body(...),
    file: UploadFile = File(...),
):
    controller: MediaPutController = container.get("MediaPutController")
    return await controller.run(id, media, file)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Delete Media")
async def delete(
    id: Annotated[str, Path(..., description="Id of the Media", example="123e4567-e89b-12d3-a456-426614174000")]
):
    controller: MediaDeleteController = container.get("MediaDeleteController")
    return await controller.run(id)


@router.get("/{id}/file", status_code=status.HTTP_200_OK, description="Find Media File")
async def get_stream(
    id: Annotated[str, Path(..., description="Id of the Media", example="123e4567-e89b-12d3-a456-426614174000")],
    range: Annotated[str, Header(..., description="Range", example="bytes=0-100")],
):
    controller: MediaFileGetController = container.get("MediaFileGetController")
    return await controller.run(id, range)
