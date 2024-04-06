from fastapi import APIRouter, Path, Query, Request, status
from typing_extensions import Annotated

from ..dependecy_injection import container
from ..schemas import (
    ChannelCreateSchema,
    ChannelGetSchema,
    ChannelPaginatedResponseSchema,
    ChannelUpdateSchema,
)

router = APIRouter(prefix="/channels", tags=["Channels"])


@router.get(
    "",
    response_model=ChannelPaginatedResponseSchema,
    status_code=status.HTTP_200_OK,
    description="Get all Channels",
)
async def search(request: Request):
    controller = container.get("ChannelsGetController")
    return controller.run(request)


@router.get(
    "/{id}",
    response_model=ChannelGetSchema,
    status_code=status.HTTP_200_OK,
    description="Find Channel",
)
async def find(
    request: Request,
    id: Annotated[
        str,
        Path(
            ...,
            description="Id of the Channel",
            example="123e4567-e89b-12d3-a456-426614174000",
        ),
    ],
):
    controller = container.get("ChannelGetController")
    return controller.run(request)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    description="Create Channel",
)
async def create(request: Request, channel: ChannelCreateSchema):
    controller = container.get("ChannelPostController")
    return await controller.run(request)


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    description="Update Channel",
)
async def update(
    request: Request,
    id: Annotated[
        str,
        Path(
            ...,
            description="Id of the Channel",
            example="123e4567-e89b-12d3-a456-426614174000",
        ),
    ],
    channel: ChannelUpdateSchema,
):
    controller = container.get("ChannelPutController")
    return await controller.run(request)


@router.delete(
    "/{id}",
    status_code=status.HTTP_200_OK,
    description="Delete Channel",
)
async def delete(
    request: Request,
    id: Annotated[
        str,
        Path(
            ...,
            description="Id of the Channel",
            example="123e4567-e89b-12d3-a456-426614174000",
        ),
    ],
):
    controller = container.get("ChannelDeleteController")
    return await controller.run(request)


@router.get(
    "/{id}/rating",
    status_code=status.HTTP_200_OK,
    description="Get Channel Rating",
)
async def rating(
    request: Request,
    id: Annotated[
        str,
        Path(
            ...,
            description="Id of the Channel",
            example="123e4567-e89b-12d3-a456-426614174000",
        ),
    ],
):
    controller = container.get("ChannelRatingGetController")
    return controller.run(request)
