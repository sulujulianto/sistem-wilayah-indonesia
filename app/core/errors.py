from __future__ import annotations

from typing import Any

from fastapi import HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def build_error(
    status_code: int,
    code: str,
    message: str,
    details: Any | None = None,
) -> HTTPException:
    return HTTPException(
        status_code=status_code,
        detail={"error": {"code": code, "message": message, "details": details}},
    )


async def http_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    if not isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=500,
            content={
                "error": {
                    "code": "server_error",
                    "message": str(exc),
                    "details": None,
                }
            },
        )

    detail = exc.detail
    if isinstance(detail, dict) and "error" in detail:
        content = detail
    else:
        content = {
            "error": {
                "code": str(exc.status_code),
                "message": str(detail),
                "details": None,
            }
        }
    return JSONResponse(status_code=exc.status_code, content=content)


async def validation_exception_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    if isinstance(exc, RequestValidationError):
        content = {
            "error": {
                "code": "validation_error",
                "message": "Invalid request",
                "details": exc.errors(),
            }
        }
        return JSONResponse(status_code=422, content=content)
    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "validation_error",
                "message": str(exc),
                "details": None,
            }
        },
    )
