from __future__ import annotations

from app.core.config import settings
from app.services.wilayah_service import WilayahService

wilayah_service = WilayahService(settings.data_path)
