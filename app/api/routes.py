from __future__ import annotations

from fastapi import APIRouter, Query

from app.core.config import settings
from app.core.errors import build_error
from app.schemas.wilayah import (
    ErrorResponse,
    HealthResponse,
    Province,
    ProvinceListResponse,
    SearchResult,
    SearchResponse,
    SearchType,
    StatsResponse,
)
from app.services.wilayah_service import WilayahService

router = APIRouter()
service = WilayahService(settings.data_path)


@router.get("/health", response_model=HealthResponse)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/v1/stats", response_model=StatsResponse)
async def get_stats() -> StatsResponse:
    return StatsResponse(**service.get_stats())


@router.get(
    "/v1/provinces",
    response_model=ProvinceListResponse,
    responses={422: {"model": ErrorResponse}},
)
async def list_provinces(
    limit: int = Query(20, ge=1, le=200),
    offset: int = Query(0, ge=0),
) -> ProvinceListResponse:
    items, total = service.list_provinces(limit=limit, offset=offset)
    province_models = [Province(**item) for item in items]
    return ProvinceListResponse(
        count=total, limit=limit, offset=offset, items=province_models
    )


@router.get(
    "/v1/provinces/{name}",
    response_model=Province,
    responses={404: {"model": ErrorResponse}, 409: {"model": ErrorResponse}},
)
async def get_province(name: str) -> Province:
    province, candidates = service.get_province(name)
    if candidates:
        raise build_error(
            status_code=409,
            code="ambiguous_province",
            message="Query matches multiple provinces",
            details={"candidates": candidates},
        )
    if province is None:
        raise build_error(
            status_code=404,
            code="province_not_found",
            message=f"Provinsi '{name}' tidak ditemukan",
        )
    return Province(**province)


@router.get(
    "/v1/search",
    response_model=SearchResponse,
    responses={422: {"model": ErrorResponse}},
)
async def search(
    q: str = Query(..., min_length=1),
    search_type: SearchType = Query(SearchType.all, alias="type"),
) -> SearchResponse:
    results = service.search(q, search_type.value)
    result_models = [SearchResult(**result) for result in results]
    return SearchResponse(
        query=q, type=search_type, count=len(result_models), results=result_models
    )
