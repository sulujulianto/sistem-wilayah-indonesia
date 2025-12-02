from __future__ import annotations

from fastapi import APIRouter, Query

from app.api import deps
from app.core.errors import build_error
from app.schemas.wilayah import ErrorResponse, Province, ProvinceListResponse

router = APIRouter()


@router.get(
    "/v1/provinces",
    response_model=ProvinceListResponse,
    responses={422: {"model": ErrorResponse}},
)
async def list_provinces(
    limit: int = Query(20, ge=1, le=200),
    offset: int = Query(0, ge=0),
) -> ProvinceListResponse:
    items, total = deps.wilayah_service.list_provinces(limit=limit, offset=offset)
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
    province, candidates = deps.wilayah_service.get_province(name)
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
