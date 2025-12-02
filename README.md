# Sistem Informasi Wilayah Indonesia (API + CLI)

FastAPI backend + CLI untuk data provinsi/kabupaten/kota. Snapshot dataset 2024-12 mencakup 38 provinsi, 416 kabupaten, 98 kota.

## Versi
- Tag v1.0.0-cli (CLI/library lama)
- Versi API: 0.1.0-api (branch feat/backend-api)
- Swagger/OpenAPI: http://127.0.0.1:8000/docs

## Quickstart Lokal
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

## Menjalankan Server (aman)
```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
Gunakan host 0.0.0.0 hanya untuk container/jaringan jika Anda paham risikonya.

## Endpoint
- GET /health
- GET /v1/stats
- GET /v1/meta
- GET /v1/provinces?limit=&offset=
- GET /v1/provinces/{name} (alias & case-insensitive, 409 jika ambigu)
- GET /v1/search?q=...&type=all|kabupaten|kota

## Contoh curl (127.0.0.1)
```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/v1/stats
curl http://127.0.0.1:8000/v1/meta
curl "http://127.0.0.1:8000/v1/provinces?limit=5&offset=0"
curl http://127.0.0.1:8000/v1/provinces/jabar
curl "http://127.0.0.1:8000/v1/search?q=bima&type=all"
```

## Pengembangan
```bash
pytest -q
ruff check .
mypy app
```

## Data
- app/data/wilayah.json
- app/data/metadata.json
- Catatan: dataset snapshot kompilasi (2024-12) dan belum diverifikasi penuh terhadap dokumen pemutakhiran resmi tahun 2025.

## Docker / Podman (opsional; CI memverifikasi docker build)
```bash
# Docker
docker build -t sistem-wilayah-indonesia-api .
docker run -p 8000:8000 sistem-wilayah-indonesia-api

# Podman
podman build -t sistem-wilayah-indonesia-api .
podman run -p 8000:8000 sistem-wilayah-indonesia-api
```

## Struktur Project (ringkas)
```
app/
  api/
  core/
  schemas/
  services/
  data/
sistem_wilayah_indonesia.py
```
