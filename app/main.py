from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from app.api.router import api_router
from app.core.config import settings
from app.core.errors import http_exception_handler, validation_exception_handler
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=settings.description,
)

if settings.allow_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allow_origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.api_route("/", methods=["GET", "HEAD"], include_in_schema=False)
async def root_redirect() -> RedirectResponse:
    return RedirectResponse(url="/docs", status_code=307)
