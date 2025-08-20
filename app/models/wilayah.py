from typing import List, Optional
from pydantic import BaseModel

class WilayahBase(BaseModel):
    nama: str
    ibu_kota: str
    kabupaten: List[str]
    kota: List[str]

class Provinsi(WilayahBase):
    total_kabupaten: int
    total_kota: int

class KabupatenKota(BaseModel):
    nama: str
    jenis: str
    provinsi: str
    ibu_kota_provinsi: str

class StatistikWilayah(BaseModel):
    total_provinsi: int
    total_kabupaten: int
    total_kota: int
    total_wilayah: int

class ProvinsiAcak(Provinsi):
    pass

class SearchResult(BaseModel):
    query: str
    results: List[KabupatenKota]