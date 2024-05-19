from fastapi import APIRouter, Body, Depends, File, Form, Header, Path, Query, Request, UploadFile, status
from typing_extensions import Annotated

from ..dependecy_injection import container
from ..schemas import MovieCreateSchema, MovieGetSchema, MoviePaginatedResponseSchema, MovieUpdateSchema

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("", response_model=MoviePaginatedResponseSchema, status_code=status.HTTP_200_OK, description="Search Movie")
async def search(
    request: Request,
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
    ] = None,
):
    controller = container.get("MoviesGetController")
    return controller.run(request)


@router.get("/{id}", response_model=MovieGetSchema, status_code=status.HTTP_200_OK, description="Find Movie")
async def find(
    request: Request,
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")],
):
    controller = container.get("MovieGetController")
    return controller.run(request)


@router.get("/{id}/file", status_code=status.HTTP_200_OK, description="Find Movie File")
async def get_stream(
    request: Request,
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")],
    file_name: Annotated[str, Query(..., description="File Name", example="file.txt")],
    range: Annotated[str, Header(..., description="Range", example="bytes=0-100")],
):
    controller = container.get("MovieFileGetController")
    return await controller.run(request)


@router.post("", status_code=status.HTTP_201_CREATED, description="Create Movie")
async def create(
    request: Request,
    rating: Annotated[float, Form(..., description="Rating", example=4.5)],
    metadata_: Annotated[str, Form(..., description="Metadata", example='{"title": "Amazing movie"}')],
    channel_id: Annotated[str, Form(..., description="Channel ID", example="123e4567-e89b-12d3-a456-426614174000")],
    files: list[UploadFile] = File(...),
):
    controller = container.get("MoviePostController")
    return await controller.run(request)


@router.put("/{id}", status_code=status.HTTP_200_OK, description="Update Movie")
async def update(
    request: Request,
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")],
    content: MovieUpdateSchema,
):
    controller = container.get("MoviePutController")
    return await controller.run(request)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Delete Movie")
async def delete(
    request: Request,
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")],
):
    controller = container.get("MovieDeleteController")
    return await controller.run(request)
