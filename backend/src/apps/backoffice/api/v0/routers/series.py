from fastapi import APIRouter, Header, Path, Query, status
from typing_extensions import Annotated

from ..dependecy_injection import container
from ..schemas import SerieCreateSchema, SerieGetSchema, SeriePaginatedResponseSchema, SerieUpdateSchema

router = APIRouter(prefix="/series", tags=["Series"])


@router.get("", response_model=SeriePaginatedResponseSchema, status_code=status.HTTP_200_OK, description="Search Serie")
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
    controller = container.get("SeriesGetController")
    return controller.run(criteria)


@router.get("/{id}", response_model=SerieGetSchema, status_code=status.HTTP_200_OK, description="Find Serie")
async def find(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")]
):
    controller = container.get("SerieGetController")
    return controller.run(id)


@router.post("", status_code=status.HTTP_201_CREATED, description="Create Serie")
async def create(serie: SerieCreateSchema):
    controller = container.get("SeriePostController")
    return await controller.run(serie)


@router.put("/{id}", status_code=status.HTTP_200_OK, description="Update Serie")
async def update(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")],
    serie: SerieUpdateSchema,
):
    controller = container.get("SeriePutController")
    return await controller.run(id, serie)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Delete Serie")
async def delete(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")]
):
    controller = container.get("SerieDeleteController")
    return await controller.run(id)


@router.get("/{id}/file", status_code=status.HTTP_200_OK, description="Find Serie File")
async def get_stream(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")],
    file_name: Annotated[str, Query(..., description="File Name", example="file.txt")],
    range: Annotated[str, Header(..., description="Range", example="bytes=0-100")],
):
    controller = container.get("SerieFileGetController")
    return await controller.run(id, file_name, range)
