from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import JSONResponse

from src.apps.channel.api.v0.exception import EXCEPTION_TO_HTTP_STATUS_CODE

from .routers import channel_router, content_router, health_check_router

app = FastAPI(
    title="Media Platform - API",
    description="This is the API documentation for the Media Platform API.",
    version="0.1.0",
    root_path="/api/v0",
    docs_url=None,
    redoc_url=None,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(router=health_check_router)
app.include_router(router=channel_router)
app.include_router(router=content_router)


# Setups the exception handler
@app.exception_handler(Exception)
def exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        content={"message": str(exception)},
        status_code=EXCEPTION_TO_HTTP_STATUS_CODE.get(
            exception.__class__, 500
        ),
    )


@app.get("/swagger", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Media Platform - API",
    )


@app.get("/documentation", include_in_schema=False)
def overridden_redoc():
    return get_redoc_html(
        openapi_url="/openapi.json",
        title="Media Platform - API",
    )
