# Sistem Informasi Wilayah Indonesia (API + CLI)

FastAPI backend dan library CLI untuk data provinsi, kabupaten, dan kota di Indonesia. Data terbaru mencakup 38 provinsi, 416 kabupaten, dan 98 kota.

## Versi & Rilisan
- Tag `v1.0.0-cli`: rilis CLI/library lama (tetap kompatibel).
- Branch `feat/backend-api` (`0.1.0-api`): rilis API portfolio dengan struktur backend, Docker, CI, lint, dan typing.

## Cepat Mulai (Local Dev)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```
Buka `http://localhost:8000/docs` untuk Swagger UI.

## API Endpoint
- `GET /health` → status service.
- `GET /v1/stats` → statistik provinsi/kabupaten/kota.
- `GET /v1/provinces?limit=&offset=` → daftar provinsi (paginasi).
- `GET /v1/provinces/{name}` → detail provinsi (alias & case-insensitive, 409 jika ambigu).
- `GET /v1/search?q=...&type=all|kabupaten|kota` → pencarian kab/kota lintas provinsi.

Contoh curl:
```bash
curl http://localhost:8000/health
curl "http://localhost:8000/v1/provinces?limit=10&offset=0"
curl http://localhost:8000/v1/provinces/jabar
curl "http://localhost:8000/v1/search?q=bima&type=all"
```

## Docker
```bash
docker build -t sistem-wilayah-indonesia-api .
docker run -p 8000:8000 sistem-wilayah-indonesia-api
# lalu akses http://localhost:8000/health atau /docs
```

## Pengembangan
- Tes: `pytest -q`
- Lint: `ruff check .`
- Typing: `mypy app`

## Struktur Project
```
app/
  main.py
  api/
  core/
  schemas/
  services/
  data/wilayah.json
sistem_wilayah_indonesia.py  # CLI/library lama (fallback ke data embedded)
```

## Sumber Data
Ringkasan: Kemendagri (Permendagri No. 137/2017), BPS, dan Wikipedia (2024). Detail metodologi berada di `DATA_SOURCES.md`.

## Lisensi
MIT License. Data mengikuti lisensi sumber masing-masing.
