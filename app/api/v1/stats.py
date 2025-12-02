from __future__ import annotations

from fastapi import APIRouter

from app.api import deps
from app.schemas.wilayah import StatsResponse

router = APIRouter()


@router.get("/v1/stats", response_model=StatsResponse)
async def get_stats() -> StatsResponse:
    return StatsResponse(**deps.wilayah_service.get_stats())
