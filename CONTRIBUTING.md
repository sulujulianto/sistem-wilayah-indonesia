# Kontribusi ke Sistem Wilayah Indonesia

Terima kasih sudah ingin berkontribusi! Panduan singkat ini membantu Anda menyiapkan lingkungan dan menjaga kualitas.

## Prasyarat
- Python 3.12+
- Git

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

## Menjalankan Server
```bash
make dev
```

## Quality Gate
```bash
make check   # pytest + ruff + mypy
make smoke   # smoke test endpoint (dapat auto-start server)
```

Jika server sudah berjalan, jalankan `SMOKE_START_SERVER=0 ./scripts/smoke_test.sh`.

## Perubahan Data
- Update `app/data/wilayah.json` dan `app/data/metadata.json` bersamaan jika ada perubahan.
- Setelah mengubah data, jalankan `make check` dan `make smoke`.

## Standar Kode
- Lint (ruff) dan type check (mypy) wajib hijau.
- Tes (pytest) wajib hijau.
- Hindari menambah dependency tanpa alasan kuat.

## Pull Request
- Jelaskan tujuan perubahan dan pengaruhnya pada API/CLI.
- Sertakan hasil `make check` dan `make smoke`.
- Jika menyentuh data, sebutkan sumber pembaruan di deskripsi PR.
