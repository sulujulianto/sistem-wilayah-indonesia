from __future__ import annotations

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from app.api.routes import router
from app.core.config import settings
from app.core.errors import http_exception_handler, validation_exception_handler
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description=settings.description,
)

app.include_router(router)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
