import random
from typing import Dict, List, Optional
from app.utils.helpers import load_wilayah_data, build_alias_map, resolve_prov, _norm

class WilayahService:
    def __init__(self):
        """Inisialisasi service dengan data wilayah."""
        self.data_wilayah = load_wilayah_data()
        self.alias_map = build_alias_map(self.data_wilayah)
        self._calculate_stats()
    
    def _calculate_stats(self) -> None:
        """Menghitung statistik data wilayah."""
        self.total_provinsi: int = len(self.data_wilayah)
        self.total_kabupaten: int = sum(len(d["kabupaten"]) for d in self.data_wilayah.values())
        self.total_kota: int = sum(len(d["kota"]) for d in self.data_wilayah.values())
    
    def cari_provinsi(self, nama_provinsi: str) -> Optional[Dict]:
        """Mencari informasi provinsi berdasarkan nama."""
        prov_name = resolve_prov(nama_provinsi, self.alias_map, self.data_wilayah)
        if not prov_name:
            return None
        data = self.data_wilayah[prov_name]
        return {
            "nama": prov_name,
            "ibu_kota": data["ibu_kota"],
            "kabupaten": list(data["kabupaten"]),
            "kota": list(data["kota"]),
            "total_kabupaten": len(data["kabupaten"]),
            "total_kota": len(data["kota"]),
        }
    
    def cari_kabupaten_kota(self, nama_wilayah: str) -> Optional[List[Dict]]:
        """Mencari kabupaten/kota di seluruh Indonesia (substring & case-insensitive)."""
        q = _norm(nama_wilayah)
        if not q:
            return None
        hasil: List[Dict] = []
        for provinsi, data in self.data_wilayah.items():
            for kab in data["kabupaten"]:
                nm = _norm(kab)
                if q in nm or nm in q:
                    hasil.append({
                        "nama": kab,
                        "jenis": "Kabupaten",
                        "provinsi": provinsi,
                        "ibu_kota_provinsi": data["ibu_kota"],
                    })
            for kota in data["kota"]:
                nm = _norm(kota)
                if q in nm or nm in q:
                    hasil.append({
                        "nama": kota,
                        "jenis": "Kota",
                        "provinsi": provinsi,
                        "ibu_kota_provinsi": data["ibu_kota"],
                    })
        return hasil or None
    
    def dapatkan_provinsi_acak(self, kecuali_provinsi: str | None = None) -> Dict:
        """Mendapatkan provinsi dan informasinya secara acak (opsional pengecualian)."""
        items = list(self.data_wilayah.items())
        if kecuali_provinsi:
            resolved = resolve_prov(kecuali_provinsi, self.alias_map, self.data_wilayah)
            if resolved:
                items = [it for it in items if it[0] != resolved]
        provinsi_terpilih = random.choice(items)
        return {
            "nama": provinsi_terpilih[0],
            **provinsi_terpilih[1],
            "total_kabupaten": len(provinsi_terpilih[1]["kabupaten"]),
            "total_kota": len(provinsi_terpilih[1]["kota"]),
        }
    
    def dapatkan_statistik(self) -> Dict[str, int]:
        """Mendapatkan statistik wilayah Indonesia."""
        return {
            "total_provinsi": self.total_provinsi,
            "total_kabupaten": self.total_kabupaten,
            "total_kota": self.total_kota,
            "total_wilayah": self.total_kabupaten + self.total_kota,
        }
    
    def dapatkan_semua_provinsi(self) -> List[Dict]:
        """Mendapatkan daftar semua provinsi."""
        provinsi_list = []
        for nama, data in self.data_wilayah.items():
            provinsi_list.append({
                "nama": nama,
                "ibu_kota": data["ibu_kota"],
                "total_kabupaten": len(data["kabupaten"]),
                "total_kota": len(data["kota"]),
            })
        return provinsi_list