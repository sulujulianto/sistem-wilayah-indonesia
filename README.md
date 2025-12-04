# Sistem Informasi Wilayah Indonesia (API + CLI)
![CI](https://github.com/sulujulianto/sistem-wilayah-indonesia/actions/workflows/ci.yml/badge.svg) ![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

FastAPI backend + CLI untuk data provinsi/kabupaten/kota. Snapshot dataset 2024-12 dengan cakupan 38 provinsi, 416 kabupaten, 98 kota. Terakhir dicek internal: Agustus 2025 (cek konsistensi coverage & struktur; bukan verifikasi legal/administratif).

## Fitur Utama
- Data provinsi/kabupaten/kota tersimpan di JSON
- Endpoint versi `/v1` (health, stats, meta, provinces, search)
- Pagination untuk daftar provinsi
- Pencarian lintas provinsi/kabupaten/kota
- Caching headers (`Cache-Control`, `ETag`) dengan dukungan `304`
- CORS bisa dikonfigurasi via env `ALLOW_ORIGINS`
- CLI legacy tetap ada (tag `v1.0.0-cli`)

## Versi & Rilis
- CLI legacy: tag `v1.0.0-cli`
- API: `v0.1.0-api`, `v0.1.1-api`, `v0.1.2-api` (terkini; mencakup smoke test & `api.http`)
- Catatan perubahan: lihat `CHANGELOG.md`; sumber data & metodologi: `DATA_SOURCES.md`

## Status Hosting
- Base URL (Production): belum tersedia (belum ada hosting publik/gratis).
- API dapat dijalankan lokal < 2 menit; sertakan `make smoke` untuk verifikasi cepat.

## Quickstart Lokal
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
make dev
```

## Verifikasi Cepat (wajib untuk reviewer)
```bash
make check
make smoke
# atau jika server sudah jalan:
SMOKE_START_SERVER=0 ./scripts/smoke_test.sh
```

## Endpoint
- `GET /health` — status aplikasi
- `GET/HEAD /v1/stats` — ringkasan total provinsi/kabupaten/kota
- `GET/HEAD /v1/meta` — metadata dataset + computed coverage
- `GET/HEAD /v1/provinces?limit=&offset=` — daftar provinsi (paginasi)
- `GET/HEAD /v1/provinces/{name}` — detail provinsi, alias & case-insensitive, `409` jika ambigu
- `GET/HEAD /v1/search?q=...&type=all|kabupaten|kota` — pencarian lintas provinsi
- Dokumentasi lokal: http://127.0.0.1:8000/docs

## Contoh Permintaan
```bash
curl http://127.0.0.1:8000/health
curl http://127.0.0.1:8000/v1/meta
curl "http://127.0.0.1:8000/v1/provinces?limit=5&offset=0"
curl http://127.0.0.1:8000/v1/provinces/jabar
curl "http://127.0.0.1:8000/v1/search?q=bima&type=all"
```
- File `api.http` siap dipakai di VS Code/JetBrains REST Client (opsional).

## Konfigurasi (ENV)
- `APP_VERSION` (default `0.1.2-api`)
- `ALLOW_ORIGINS` (pisah dengan koma; kosongkan untuk menonaktifkan CORS)
- `PORT` (default 8000)
- Jalankan dengan host `127.0.0.1`; gunakan `0.0.0.0` hanya jika memahami risikonya (container/jaringan).

## Data & Atribusi
- Dataset snapshot: `dataset_version` 2024-12; coverage: 38 provinsi, 416 kabupaten, 98 kota.
- `last_updated` pada metadata merefleksikan tanggal file di repo, bukan klaim perubahan administratif resmi.
- Untuk akurasi legal/administratif, rujuk sumber resmi; detail sumber & atribusi ada di `DATA_SOURCES.md`.
- Lisensi kode: MIT (lihat `LICENSE`); lisensi data mengikuti sumber masing-masing.

## Kontribusi
Lihat `CONTRIBUTING.md` untuk panduan setup, quality gate, smoke test, dan aturan perubahan data.
