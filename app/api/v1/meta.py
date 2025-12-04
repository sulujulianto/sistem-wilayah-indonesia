from __future__ import annotations

from fastapi import APIRouter, Request, Response

from app.api import deps
from app.core.cache import CACHE_CONTROL_HEADER_VALUE
from app.core.errors import build_error
from app.schemas.wilayah import ErrorResponse, Metadata

router = APIRouter()


@router.api_route(
    "/v1/meta",
    methods=["GET", "HEAD"],
    response_model=Metadata,
    responses={404: {"model": ErrorResponse}},
)
async def get_metadata(request: Request, response: Response) -> Metadata | Response:
    etag = deps.get_data_etag()
    if request.headers.get("if-none-match") == etag:
        return Response(
            status_code=304,
            headers={"ETag": etag, "Cache-Control": CACHE_CONTROL_HEADER_VALUE},
        )
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
    response.headers["Cache-Control"] = CACHE_CONTROL_HEADER_VALUE
    response.headers["ETag"] = etag
    return Metadata(**metadata)
