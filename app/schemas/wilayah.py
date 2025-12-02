from __future__ import annotations

from enum import Enum
from typing import Any, List

from pydantic import BaseModel


class SearchType(str, Enum):
    all = "all"
    kabupaten = "kabupaten"
    kota = "kota"


class HealthResponse(BaseModel):
    status: str = "ok"


class Province(BaseModel):
    name: str
    ibu_kota: str
    kabupaten: List[str]
    kota: List[str]
    total_kabupaten: int
    total_kota: int


class ProvinceListResponse(BaseModel):
    count: int
    limit: int
    offset: int
    items: List[Province]


class StatsResponse(BaseModel):
    total_provinsi: int
    total_kabupaten: int
    total_kota: int
    total_wilayah: int


class SearchResult(BaseModel):
    name: str
    type: str
    province: str
    ibu_kota_provinsi: str


class SearchResponse(BaseModel):
    query: str
    type: SearchType
    count: int
    results: List[SearchResult]


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Any | None = None


class ErrorResponse(BaseModel):
    error: ErrorDetail
