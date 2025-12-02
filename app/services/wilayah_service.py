from __future__ import annotations

from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from sistem_wilayah_indonesia import SistemWilayahIndonesia


def _normalize(text: str) -> str:
    return " ".join(text.split()).strip().lower()


class WilayahService:
    def __init__(self, data_path: str | Path | None = None):
        path = Path(data_path) if data_path else None
        self._sistem = SistemWilayahIndonesia(data_path=path)
        self._alias_map = self._sistem.get_alias_map()

    def get_stats(self) -> Dict[str, int]:
        return self._sistem.dapatkan_statistik()

    def list_provinces(self, limit: int, offset: int) -> Tuple[List[Dict], int]:
        provinces = sorted(
            self._sistem.data_wilayah.items(), key=lambda item: _normalize(item[0])
        )
        total = len(provinces)
        sliced = provinces[offset : offset + limit]
        return [self._build_province(name, data) for name, data in sliced], total

    def get_province(self, query: str) -> Tuple[Dict | None, List[str]]:
        candidates = self._province_candidates(query)
        if not candidates:
            return None, []
        if len(candidates) > 1:
            return None, sorted(candidates, key=_normalize)
        name = candidates[0]
        return self._build_province(name, self._sistem.data_wilayah[name]), []

    def search(self, query: str, search_type: str = "all") -> List[Dict]:
        q = _normalize(query)
        if not q:
            return []
        results: List[Dict] = []
        for provinsi, data in self._sistem.data_wilayah.items():
            ibu_kota = str(data["ibu_kota"])
            results.extend(
                self._match_entries(q, data["kabupaten"], provinsi, ibu_kota, "kabupaten")
            )
            results.extend(
                self._match_entries(q, data["kota"], provinsi, ibu_kota, "kota")
            )
        if search_type != "all":
            results = [r for r in results if r["type"] == search_type]
        return results

    def _province_candidates(self, query: str) -> List[str]:
        q = _normalize(query)
        provinces = list(self._sistem.data_wilayah.keys())
        matches = [
            prov
            for prov in provinces
            if q == _normalize(prov)
            or q in _normalize(prov)
            or _normalize(prov) in q
        ]
        alias_target = self._alias_map.get(q)
        if alias_target and alias_target not in matches:
            matches.insert(0, alias_target)
        # Remove duplicates preserving order
        seen = set()
        unique: List[str] = []
        for prov in matches:
            if prov not in seen:
                seen.add(prov)
                unique.append(prov)
        return unique

    def _match_entries(
        self,
        query: str,
        entries: Iterable[str],
        provinsi: str,
        ibu_kota: str,
        entry_type: str,
    ) -> List[Dict]:
        found: List[Dict] = []
        for entry in entries:
            normalized = _normalize(entry)
            if query in normalized or normalized in query:
                found.append(
                    {
                        "name": entry,
                        "type": entry_type,
                        "province": provinsi,
                        "ibu_kota_provinsi": ibu_kota,
                    }
                )
        return found

    def _build_province(self, name: str, data: Dict) -> Dict:
        return {
            "name": name,
            "ibu_kota": data["ibu_kota"],
            "kabupaten": list(data["kabupaten"]),
            "kota": list(data["kota"]),
            "total_kabupaten": len(data["kabupaten"]),
            "total_kota": len(data["kota"]),
        }
