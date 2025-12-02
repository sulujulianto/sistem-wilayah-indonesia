from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from app.services.wilayah_service import WilayahService


class MetadataService:
    def __init__(self, metadata_path: Path):
        self.metadata_path = metadata_path

    def read_metadata(self) -> Dict[str, Any]:
        if not self.metadata_path.exists():
            raise FileNotFoundError(f"Metadata file not found at {self.metadata_path}")
        with self.metadata_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, dict):
            raise ValueError("Invalid metadata format; expected JSON object")
        return data

    def get_metadata_with_computed(self, wilayah_service: WilayahService) -> Dict[str, Any]:
        data = self.read_metadata()
        stats = wilayah_service.get_stats()
        data["computed_coverage"] = {
            "total_provinsi": stats["total_provinsi"],
            "total_kabupaten": stats["total_kabupaten"],
            "total_kota": stats["total_kota"],
        }
        return data
