from fastapi import APIRouter, HTTPException
from typing import List, Optional
from app.services.wilayah_service import WilayahService
from app.models.wilayah import (
    Provinsi, 
    KabupatenKota, 
    StatistikWilayah, 
    ProvinsiAcak, 
    SearchResult
)

router = APIRouter()
service = WilayahService()

@router.get("/provinsi", response_model=List[Provinsi])
async def get_all_provinsi():
    """Mendapatkan daftar semua provinsi."""
    provinsi_list = service.dapatkan_semua_provinsi()
    result = []
    for p in provinsi_list:
        # Cari data lengkap dari service
        detail = service.cari_provinsi(p["nama"])
        if detail:
            result.append(detail)
    return result

@router.get("/provinsi/{nama}", response_model=Provinsi)
async def get_provinsi(nama: str):
    """Mendapatkan detail provinsi berdasarkan nama."""
    provinsi = service.cari_provinsi(nama)
    if not provinsi:
        raise HTTPException(status_code=404, detail="Provinsi tidak ditemukan")
    return provinsi

@router.get("/search", response_model=SearchResult)
async def search_wilayah(q: str):
    """Mencari kabupaten/kota berdasarkan nama."""
    if not q:
        raise HTTPException(status_code=400, detail="Query parameter 'q' diperlukan")
    
    hasil = service.cari_kabupaten_kota(q)
    if not hasil:
        hasil = []
    
    return SearchResult(query=q, results=hasil)

@router.get("/stats", response_model=StatistikWilayah)
async def get_statistics():
    """Mendapatkan statistik wilayah Indonesia."""
    return service.dapatkan_statistik()

@router.get("/random", response_model=ProvinsiAcak)
async def get_random_provinsi(except_provinsi: Optional[str] = None):
    """Mendapatkan provinsi secara acak."""
    return service.dapatkan_provinsi_acak(except_provinsi)