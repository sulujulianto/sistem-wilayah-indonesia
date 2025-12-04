# Sistem Informasi Wilayah Indonesia (API + CLI)

FastAPI backend + CLI untuk data provinsi/kabupaten/kota. Snapshot dataset 2024-12 mencakup 38 provinsi, 416 kabupaten, 98 kota. Terakhir diverifikasi internal: Agustus 2025 (lihat DATA_SOURCES.md).

## Versi
- Tag v1.0.0-cli (CLI/library lama)
- Versi API: 0.1.0-api (branch feat/backend-api)
- Swagger/OpenAPI: http://127.0.0.1:8000/docs

## Base URL (Production)
- Placeholder: https://api.example.com
- Swagger: https://api.example.com/docs

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

## Contoh curl (lokal & produksi)
```bash
# Lokal
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/v1/stats
curl http://127.0.0.1:8000/v1/meta
curl "http://127.0.0.1:8000/v1/provinces?limit=5&offset=0"
curl http://127.0.0.1:8000/v1/provinces/jabar
curl "http://127.0.0.1:8000/v1/search?q=bima&type=all"

# Produksi (ganti base URL sesuai deploy)
BASE_URL=https://api.example.com
curl "$BASE_URL/health"
curl "$BASE_URL/v1/meta"
curl "$BASE_URL/v1/search?q=bima&type=all"
```

## Pengembangan
```bash
pytest -q
ruff check .
mypy app
# Smoke test (start server otomatis kecuali SMOKE_START_SERVER=0)
./scripts/smoke_test.sh
# atau
make smoke
```

## API Client (opsional)
- Gunakan `api.http` (format REST Client) di VS Code/JetBrains untuk mencoba endpoint.

## Data
- app/data/wilayah.json
- app/data/metadata.json
- Catatan: dataset snapshot kompilasi (2024-12) dan belum diverifikasi penuh terhadap dokumen pemutakhiran resmi tahun 2025; untuk kepentingan hukum, rujuk langsung ke instansi pemerintah (lihat DATA_SOURCES.md).
- Lisensi data mengikuti sumber aslinya dan membutuhkan atribusi yang sesuai; lisensi kode: MIT (lihat LICENSE). DETAIL sumber dan atribusi: DATA_SOURCES.md.

## Cache & CORS
- Respons data statis menggunakan `Cache-Control: public, max-age=86400` dan `ETag`; jika mengirim `If-None-Match`, server akan membalas `304` tanpa body.
- Aktifkan CORS dengan env `ALLOW_ORIGINS` (pisahkan koma jika banyak origin); kosongkan untuk menonaktifkan.

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

## Referensi
- CHANGELOG: CHANGELOG.md
- Sumber & metodologi: DATA_SOURCES.md
- Lisensi: LICENSE
- Deployment: DEPLOYMENT.md
