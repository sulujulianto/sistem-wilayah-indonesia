from __future__ import annotations

from fastapi import APIRouter

from app.api.v1 import health, meta, provinces, search, stats

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(stats.router)
api_router.include_router(provinces.router)
api_router.include_router(search.router)
api_router.include_router(meta.router)
