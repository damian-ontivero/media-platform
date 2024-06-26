from fastapi import APIRouter, status

from ..dependecy_injection import container

router = APIRouter(tags=["Health check"])


@router.get("/health", response_model=str, status_code=status.HTTP_200_OK)
async def health_check():
    controller = container.get("HealthCheckController")
    return await controller.run(request=None)
