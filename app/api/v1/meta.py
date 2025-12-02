from __future__ import annotations

from fastapi import APIRouter

from app.api import deps
from app.core.errors import build_error
from app.schemas.wilayah import ErrorResponse, Metadata

router = APIRouter()


@router.get("/v1/meta", response_model=Metadata, responses={404: {"model": ErrorResponse}})
async def get_metadata() -> Metadata:
    try:
        metadata = deps.metadata_service.get_metadata_with_computed(deps.wilayah_service)
    except FileNotFoundError as exc:
        raise build_error(
            status_code=404,
            code="metadata_not_found",
            message=str(exc),
        ) from exc
    except ValueError as exc:
        raise build_error(
            status_code=500,
            code="metadata_invalid",
            message=str(exc),
        ) from exc
    return Metadata(**metadata)
