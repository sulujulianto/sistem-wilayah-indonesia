from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import List

BASE_DIR = Path(__file__).resolve().parent.parent


def _resolve_data_path() -> Path:
    env_path = os.getenv("WILAYAH_DATA_PATH")
    if env_path:
        return Path(env_path)
    return BASE_DIR / "data" / "wilayah.json"


def _resolve_metadata_path() -> Path:
    env_path = os.getenv("WILAYAH_METADATA_PATH")
    if env_path:
        return Path(env_path)
    return BASE_DIR / "data" / "metadata.json"


def _load_dataset_version(metadata_path: Path) -> str:
    try:
        if metadata_path.exists():
            import json

            with metadata_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, dict) and "dataset_version" in data:
                return str(data["dataset_version"])
    except Exception:
        # Fallback handled below
        pass
    return "unknown"


@dataclass
class Settings:
    app_name: str
    version: str
    description: str
    data_path: Path
    metadata_path: Path
    dataset_version: str
    allow_origins: List[str]
    port: int


def _load_settings() -> Settings:
    data_path = _resolve_data_path()
    metadata_path = _resolve_metadata_path()
    dataset_version = _load_dataset_version(metadata_path)
    version = os.getenv("APP_VERSION", "0.1.2-api")
    description = (
        f"Sistem Wilayah Indonesia API — snapshot dataset {dataset_version}. "
        "Data provinsi, kabupaten, kota dalam format JSON."
    )
    allow_origins_env = os.getenv("ALLOW_ORIGINS", "")
    allow_origins = [origin.strip() for origin in allow_origins_env.split(",") if origin.strip()]
    port = int(os.getenv("PORT", "8000"))
    return Settings(
        app_name="Sistem Wilayah Indonesia API",
        version=version,
        description=description,
        data_path=data_path,
        metadata_path=metadata_path,
        dataset_version=dataset_version,
        allow_origins=allow_origins,
        port=port,
    )


settings = _load_settings()
