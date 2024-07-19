from fastapi import APIRouter, Path, Query, status
from src.apps.backoffice.api.v0.controllers.series.serie_delete_controller import SerieDeleteController
from src.apps.backoffice.api.v0.controllers.series.serie_get_controller import SerieGetController
from src.apps.backoffice.api.v0.controllers.series.serie_post_controller import SeriePostController
from src.apps.backoffice.api.v0.controllers.series.serie_put_controller import SeriePutController
from src.apps.backoffice.api.v0.controllers.series.series_get_controller import SeriesGetController
from src.apps.backoffice.api.v0.dependecy_injection import container
from src.apps.backoffice.api.v0.schemas.series import SeriePaginatedResponseSchema, SerieReadSchema, SerieWriteSchema
from typing_extensions import Annotated

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
    controller: SeriesGetController = container.get("SeriesGetController")
    return await controller.run(criteria)


@router.get("/{id}", response_model=SerieReadSchema, status_code=status.HTTP_200_OK, description="Find Serie")
async def find(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")]
):
    controller: SerieGetController = container.get("SerieGetController")
    return await controller.run(id)


@router.post("", status_code=status.HTTP_201_CREATED, description="Create Serie")
async def create(serie: SerieWriteSchema):
    controller: SeriePostController = container.get("SeriePostController")
    return await controller.run(serie)


@router.put("/{id}", status_code=status.HTTP_200_OK, description="Update Serie")
async def update(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")],
    serie: SerieWriteSchema,
):
    controller: SeriePutController = container.get("SeriePutController")
    return await controller.run(id, serie)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Delete Serie")
async def delete(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")]
):
    controller: SerieDeleteController = container.get("SerieDeleteController")
    return await controller.run(id)
