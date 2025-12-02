from __future__ import annotations

from fastapi import APIRouter

from app.schemas.wilayah import HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse)
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
