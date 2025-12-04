from __future__ import annotations

from fastapi import APIRouter, Query, Request, Response

from app.api import deps
from app.core.cache import CACHE_CONTROL_HEADER_VALUE
from app.schemas.wilayah import ErrorResponse, SearchResponse, SearchResult, SearchType

router = APIRouter()


@router.get(
    "/v1/search",
    response_model=SearchResponse,
    responses={422: {"model": ErrorResponse}},
)
async def search(
    request: Request,
    response: Response,
    q: str = Query(..., min_length=1),
    search_type: SearchType = Query(SearchType.all, alias="type"),
) -> SearchResponse | Response:
    etag = deps.get_data_etag()
    if request.headers.get("if-none-match") == etag:
        return Response(
            status_code=304,
            headers={"ETag": etag, "Cache-Control": CACHE_CONTROL_HEADER_VALUE},
        )
    results = deps.wilayah_service.search(q, search_type.value)
    result_models = [SearchResult(**result) for result in results]
    response.headers["Cache-Control"] = CACHE_CONTROL_HEADER_VALUE
    response.headers["ETag"] = etag
    return SearchResponse(
        query=q, type=search_type, count=len(result_models), results=result_models
    )
