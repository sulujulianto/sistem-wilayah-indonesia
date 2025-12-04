from __future__ import annotations

from fastapi import APIRouter, Request, Response

from app.api import deps
from app.core.cache import CACHE_CONTROL_HEADER_VALUE
from app.schemas.wilayah import StatsResponse

router = APIRouter()


@router.api_route(
    "/v1/stats",
    methods=["GET", "HEAD"],
    response_model=StatsResponse,
)
async def get_stats(request: Request, response: Response) -> StatsResponse | Response:
    etag = deps.get_data_etag()
    if request.headers.get("if-none-match") == etag:
        return Response(
            status_code=304,
            headers={"ETag": etag, "Cache-Control": CACHE_CONTROL_HEADER_VALUE},
        )
    response.headers["Cache-Control"] = CACHE_CONTROL_HEADER_VALUE
    response.headers["ETag"] = etag
    return StatsResponse(**deps.wilayah_service.get_stats())
