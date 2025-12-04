from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Iterable

CACHE_CONTROL_HEADER_VALUE = "public, max-age=86400"


def compute_etag(paths: Iterable[Path]) -> str:
    hasher = hashlib.sha256()
    for path in sorted(paths, key=lambda p: str(p)):
        try:
            stat = path.stat()
            hasher.update(f"{path}:{stat.st_mtime_ns}:{stat.st_size}".encode())
        except FileNotFoundError:
            hasher.update(f"{path}:missing".encode())
    return f'W/"{hasher.hexdigest()}"'
