# DEPLOYMENT

Panduan singkat menyiapkan **Sistem Wilayah Indonesia API** untuk lingkungan publik.

## Prasyarat
- Python 3.12+
- Virtual environment
- File data bawaan: `app/data/wilayah.json` dan `app/data/metadata.json`
- (Opsional) Salin `.env.example` menjadi `.env` lalu sesuaikan nilai variabel.

## Menjalankan Lokal / Development
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port ${PORT:-8000} --reload
```

## Menjalankan Production (single process)
```bash
export APP_VERSION=${APP_VERSION:-0.1.0-api}
export PORT=${PORT:-8000}
# Atur origins hanya jika perlu CORS publik, mis. ALLOW_ORIGINS=https://example.com,https://sub.example.com
export ALLOW_ORIGINS=""
python -m uvicorn app.main:app --host 0.0.0.0 --port "$PORT"
```

Gunakan reverse proxy (nginx/Caddy) untuk TLS dan buffering jika diperlukan. File data bersifat statis; respons sudah menyertakan `Cache-Control` dan `ETag` untuk efisiensi.

## Deploy ke Platform Umum (garis besar)
- **Render/Fly.io/Railway**: gunakan Dockerfile yang sudah ada. Set env `APP_VERSION`, `PORT`, `ALLOW_ORIGINS`, dan mount data jika ingin override `WILAYAH_DATA_PATH`/`WILAYAH_METADATA_PATH`.
- **VM/Bare metal**: buat service manager (systemd/supervisor) yang menjalankan perintah uvicorn production di atas.
- **Container orchestrator**: gunakan image hasil `docker build -t sistem-wilayah-indonesia-api .` dan ekspos port `8000`.

Pastikan mengecek `/health` dan `/docs` setelah deploy, serta jalankan `make check` pada pipeline sebelum merilis.
