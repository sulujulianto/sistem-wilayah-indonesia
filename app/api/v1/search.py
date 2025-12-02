from __future__ import annotations

from fastapi import APIRouter, Query

from app.api import deps
from app.schemas.wilayah import ErrorResponse, SearchResponse, SearchResult, SearchType

router = APIRouter()


@router.get(
    "/v1/search",
    response_model=SearchResponse,
    responses={422: {"model": ErrorResponse}},
)
async def search(
    q: str = Query(..., min_length=1),
    search_type: SearchType = Query(SearchType.all, alias="type"),
) -> SearchResponse:
    results = deps.wilayah_service.search(q, search_type.value)
    result_models = [SearchResult(**result) for result in results]
    return SearchResponse(
        query=q, type=search_type, count=len(result_models), results=result_models
    )
