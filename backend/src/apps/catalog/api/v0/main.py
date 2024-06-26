import dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.responses import JSONResponse

from src.apps.catalog.api.v0.exception import EXCEPTION_TO_HTTP_STATUS_CODE

from .routers import health_check_router, movies_router, series_router

dotenv.load_dotenv(".env", override=True)


app = FastAPI(
    title="Media Platform - Catalog - API",
    description="This is the API documentation for the Media Platform Catalog API.",
    version="0.1.0",
    root_path="/catalog/api/v0",
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url=None,
)

# CORS
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_credentials=False, allow_methods=["*"], allow_headers=["*"]
)

# Routers
app.include_router(router=health_check_router)
app.include_router(router=movies_router)
app.include_router(router=series_router)


# Setups the exception handler
@app.exception_handler(Exception)
def exception_handler(request: Request, exception: Exception):
    return JSONResponse(
        content={"message": str(exception)}, status_code=EXCEPTION_TO_HTTP_STATUS_CODE.get(exception.__class__, 500)
    )


@app.get("/swagger", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(title=app.title, openapi_url=app.root_path + app.openapi_url)


@app.get("/documentation", include_in_schema=False)
def overridden_redoc():
    return get_redoc_html(title=app.title, openapi_url=app.root_path + app.openapi_url)
