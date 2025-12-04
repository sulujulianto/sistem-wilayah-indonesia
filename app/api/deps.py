from __future__ import annotations

from app.core.config import settings
from app.core.cache import compute_etag
from app.services.metadata_service import MetadataService
from app.services.wilayah_service import WilayahService

wilayah_service = WilayahService(settings.data_path)
metadata_service = MetadataService(settings.metadata_path)


def get_data_etag() -> str:
    return compute_etag([settings.data_path, settings.metadata_path])
