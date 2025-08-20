import json
import os
from typing import Dict, List
from app.utils.helpers import _norm

def _norm(s: str) -> str:
    """Normalisasi string untuk pencarian yang lebih robust."""
    return " ".join(s.split()).strip().lower()

def load_wilayah_data() -> Dict[str, Dict[str, List[str] | str]]:
    """Memuat data wilayah dari file JSON."""
    file_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "wilayah_data.json")
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_alias_map(data_wilayah: Dict[str, Dict[str, List[str] | str]]) -> Dict[str, str]:
    """Membangun peta alias (nama lain) -> nama provinsi kanonik."""
    _alias_map: Dict[str, str] = {}
    for prov in data_wilayah.keys():
        _alias_map[_norm(prov)] = prov
    
    # Alias umum
    manual_alias = {
        # Aceh
        "aceh": "Nanggroe Aceh Darussalam",
        "nad": "Nanggroe Aceh Darussalam",

        # Sumatera Utara
        "sumut": "Sumatera Utara",

        # Sumatera Barat
        "sumbar": "Sumatera Barat",

        # Riau
        "riau": "Riau",

        # Kepulauan Riau
        "kepri": "Kepulauan Riau",

        # Jambi
        "jambi": "Jambi",

        # Sumatera Selatan
        "sumsel": "Sumatera Selatan",

        # Kep. Bangka Belitung
        "babel": "Kepulauan Bangka Belitung",

        # Bengkulu
        "bengkulu": "Bengkulu",

        # Lampung
        "lampung": "Lampung",

        # DKI Jakarta
        "jakarta": "DKI Jakarta",

        # Jawa Barat
        "jabar": "Jawa Barat",

        # Jawa Tengah
        "jateng": "Jawa Tengah",

        # DI Yogyakarta
        "diy": "Daerah Istimewa Yogyakarta",
        "yogyakarta": "Daerah Istimewa Yogyakarta",
        "jogja": "Daerah Istimewa Yogyakarta",

        # Jawa Timur
        "jatim": "Jawa Timur",

        # Banten
        "banten": "Banten",

        # Bali
        "bali": "Bali",

        # Nusa Tenggara Barat
        "ntb": "Nusa Tenggara Barat",

        # Nusa Tenggara Timur
        "ntt": "Nusa Tenggara Timur",

        # Kalimantan Barat
        "kalbar": "Kalimantan Barat",

        # Kalimantan Tengah
        "kalteng": "Kalimantan Tengah",

        # Kalimantan Selatan
        "kalsel": "Kalimantan Selatan",

        # Kalimantan Timur
        "kaltim": "Kalimantan Timur",

        # Kalimantan Utara
        "kaltara": "Kalimantan Utara",
        "kalut": "Kalimantan Utara",

        # Sulawesi Utara
        "sulut": "Sulawesi Utara",

        # Gorontalo
        "gorontalo": "Gorontalo",

        # Sulawesi Tengah
        "sulteng": "Sulawesi Tengah",

        # Sulawesi Barat
        "sulbar": "Sulawesi Barat",

        # Sulawesi Selatan
        "sulsel": "Sulawesi Selatan",

        # Sulawesi Tenggara
        "sultra": "Sulawesi Tenggara",

        # Maluku
        "maluku": "Maluku",

        # Maluku Utara
        "malut": "Maluku Utara",

        # Papua
        "papua": "Papua",

        # Papua Barat
        "papua barat": "Papua Barat",

        # Papua Barat Daya (DOB)
        "papua barat daya": "Papua Barat Daya",

        # Papua Tengah (DOB)
        "papua tengah": "Papua Tengah",

        # Papua Selatan (DOB)
        "papua selatan": "Papua Selatan",

        # Papua Pegunungan (DOB)
        "papua pegunungan": "Papua Pegunungan",
    }
    
    for k, v in manual_alias.items():
        _alias_map[k] = v
    
    return _alias_map

def resolve_prov(nama_provinsi: str, alias_map: Dict[str, str], data_wilayah: Dict[str, Dict[str, List[str] | str]]) -> str | None:
    key = _norm(nama_provinsi)
    if key in alias_map:
        return alias_map[key]
    # fallback substring match
    for prov in data_wilayah.keys():
        if key in _norm(prov) or _norm(prov) in key:
            return prov
    return None