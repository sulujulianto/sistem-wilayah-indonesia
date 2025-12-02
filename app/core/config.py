from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def _resolve_data_path() -> Path:
    env_path = os.getenv("WILAYAH_DATA_PATH")
    if env_path:
        return Path(env_path)
    return BASE_DIR / "data" / "wilayah.json"


@dataclass
class Settings:
    app_name: str = "Sistem Wilayah Indonesia API"
    version: str = "0.1.0-api"
    description: str = (
        "FastAPI service exposing Indonesian provinces, kabupaten, and kota data"
    )
    data_path: Path = _resolve_data_path()


settings = Settings()
