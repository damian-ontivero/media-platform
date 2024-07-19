from fastapi import APIRouter, Path, Query, status
from src.apps.backoffice.api.v0.controllers.movies.movie_delete_controller import MovieDeleteController
from src.apps.backoffice.api.v0.controllers.movies.movie_get_controller import MovieGetController
from src.apps.backoffice.api.v0.controllers.movies.movie_post_controller import MoviePostController
from src.apps.backoffice.api.v0.controllers.movies.movie_put_controller import MoviePutController
from src.apps.backoffice.api.v0.controllers.movies.movies_get_controller import MoviesGetController
from src.apps.backoffice.api.v0.dependecy_injection import container
from src.apps.backoffice.api.v0.schemas.movies import MoviePaginatedResponseSchema, MovieReadSchema, MovieWriteSchema
from typing_extensions import Annotated

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("", response_model=MoviePaginatedResponseSchema, status_code=status.HTTP_200_OK, description="Search Movie")
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
    controller: MoviesGetController = container.get("MoviesGetController")
    return await controller.run(criteria)


@router.get("/{id}", response_model=MovieReadSchema, status_code=status.HTTP_200_OK, description="Find Movie")
async def find(
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")]
):
    controller: MovieGetController = container.get("MovieGetController")
    return await controller.run(id)


@router.post("", status_code=status.HTTP_201_CREATED, description="Create Movie")
async def create(movie: MovieWriteSchema):
    controller: MoviePostController = container.get("MoviePostController")
    return await controller.run(movie)


@router.put("/{id}", status_code=status.HTTP_200_OK, description="Update Movie")
async def update(
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")],
    movie: MovieWriteSchema,
):
    controller: MoviePutController = container.get("MoviePutController")
    return await controller.run(id, movie)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Delete Movie")
async def delete(
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")]
):
    controller: MovieDeleteController = container.get("MovieDeleteController")
    return await controller.run(id)
