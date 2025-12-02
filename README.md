# Sistem Informasi Wilayah Indonesia (API + CLI)

Backend FastAPI dan CLI untuk data provinsi, kabupaten, dan kota di Indonesia. Dataset memuat 38 provinsi, 416 kabupaten, dan 98 kota (update 2024-12).

## Versi & Rilisan
- Tag `v1.0.0-cli`: rilis CLI/library lama (tetap kompatibel, fallback data embedded).
- Versi API: `0.1.0-api` (branch `feat/backend-api`) dengan endpoint terstruktur, lint/typing, Docker, dan CI.
- OpenAPI/Swagger tersedia di `http://localhost:8000/docs`.

## Quickstart Lokal
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

### Menjalankan Server
- Dev (auto-reload):
  ```bash
  uvicorn app.main:app --reload
  ```
- Prod lokal:
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000
  ```

## API Endpoint
- `GET /health` → status service.
- `GET /v1/stats` → statistik provinsi/kabupaten/kota.
- `GET /v1/meta` → metadata dataset (versi, sumber, coverage + computed_coverage).
- `GET /v1/provinces?limit=&offset=` → daftar provinsi (paginasi).
- `GET /v1/provinces/{name}` → detail provinsi (alias & case-insensitive, 409 jika ambigu).
- `GET /v1/search?q=...&type=all|kabupaten|kota` → pencarian lintas provinsi.

Contoh curl:
```bash
curl http://localhost:8000/health
curl "http://localhost:8000/v1/stats"
curl "http://localhost:8000/v1/meta"
curl "http://localhost:8000/v1/provinces?limit=5&offset=0"
curl http://localhost:8000/v1/provinces/jabar
curl "http://localhost:8000/v1/search?q=bima&type=all"
```

## Pengembangan
- Tes: `pytest -q`
- Lint: `ruff check .`
- Typing: `mypy app`

## Data & Pembaruan
- Data wilayah: `app/data/wilayah.json`
- Metadata: `app/data/metadata.json` (dataset_name, dataset_version, last_updated, source_notes, coverage)
- Sumber ringkas: Permendagri 137/2017, BPS, dan Wikipedia (2024). Detail metodologi ada di `DATA_SOURCES.md`.
- Cara update data: perbarui `wilayah.json` dan sesuaikan `metadata.json` (coverage & last_updated). Pastikan format JSON rapi (indent 2, UTF-8) dan jalankan kembali tes (pytest, ruff, mypy).

## Docker
```bash
docker build -t sistem-wilayah-indonesia-api .
docker run -p 8000:8000 sistem-wilayah-indonesia-api
```

## Struktur Project (ringkas)
```
app/
  main.py
  api/
    router.py
    v1/
  core/
  schemas/
  services/
  data/
    wilayah.json
    metadata.json
sistem_wilayah_indonesia.py  # CLI/library lama (fallback data embedded)
```

## Lisensi
MIT License. Data mengikuti lisensi sumber masing-masing.
