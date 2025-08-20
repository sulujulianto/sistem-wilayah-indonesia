# 🗺️ Sistem Informasi Wilayah Indonesia API

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)

API RESTful komprehensif untuk mencari data provinsi, ibu kota, kabupaten, dan kota di Indonesia — data update hingga Agustus 2025.

---

## 📋 Deskripsi

API ini menyediakan akses mudah ke informasi administratif wilayah Indonesia, termasuk:
- **38 Provinsi** dengan ibu kotanya
- **416 Kabupaten**
- **98 Kota**
- Total **514** wilayah administratif tingkat kedua

Versi terbaru merupakan konversi dari aplikasi CLI ke RESTful API menggunakan framework FastAPI.

---

## 🎯 Fitur Utama

### 🔍 Pencarian Wilayah
- Pencarian provinsi (tampilkan ibu kota, jumlah kabupaten/kota)
- Pencarian kabupaten/kota (tampilkan provinsi & ibu kota provinsi)
- Fuzzy search (pencarian partial/substring)

### 📊 Statistik & Informasi
- Statistik nasional: jumlah provinsi, kabupaten, dan kota
- "Fun fact" provinsi acak
- Daftar lengkap provinsi

### 💾 Export Data
- Export ke JSON (.json) dan TXT (.txt)
- File export diberi timestamp otomatis
- Folder `data_export/` akan dibuat otomatis saat export pertama

### 🎨 API Features
- RESTful API dengan endpoint yang jelas
- Dokumentasi API otomatis dengan Swagger UI dan ReDoc
- Validasi data dengan Pydantic
- Penanganan error yang informatif
- Support CORS untuk integrasi frontend

---

## 📚 Sumber Data

Data digabungkan dan diverifikasi dari:
1. **Peraturan Menteri Dalam Negeri No. 137 Tahun 2017** — kode & data wilayah administratif (Kemendagri).
2. **Wikipedia (2024)** — kompilasi kabupaten/kota per provinsi (verifikasi silang).
3. **Badan Pusat Statistik (BPS)** — data statistik & validasi.

Detail sumber dan metodologi ada di `DATA_SOURCES.md`.

---

## ⚙️ Instalasi

### Prasyarat
- Python 3.7 atau lebih baru
- Git (opsional)

### Cara cepat
```bash
git clone https://github.com/username/sistem-wilayah-indonesia.git
cd sistem-wilayah-indonesia
python -m venv venv
# activate venv:
# macOS / Linux:
source venv/bin/activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python run.py
```

---

## 🚀 Penggunaan (API)

### Menjalankan Server
```bash
python run.py
```

Server akan berjalan di `http://localhost:8000`

### Endpoint API

| Endpoint | Method | Deskripsi |
|---------|--------|-----------|
| `/` | GET | Halaman utama API |
| `/health` | GET | Health check endpoint |
| `/api/v1/provinsi` | GET | Mendapatkan semua provinsi |
| `/api/v1/provinsi/{nama}` | GET | Mendapatkan detail provinsi |
| `/api/v1/search?q={query}` | GET | Mencari kabupaten/kota |
| `/api/v1/stats` | GET | Mendapatkan statistik wilayah |
| `/api/v1/random` | GET | Mendapatkan provinsi acak |

### Dokumentasi API
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Contoh Penggunaan API

#### Mendapatkan semua provinsi:
```bash
curl http://localhost:8000/api/v1/provinsi
```

#### Mendapatkan detail provinsi:
```bash
curl http://localhost:8000/api/v1/provinsi/Jawa%20Barat
```

#### Mencari wilayah:
```bash
curl "http://localhost:8000/api/v1/search?q=bandung"
```

#### Mendapatkan statistik:
```bash
curl http://localhost:8000/api/v1/stats
```

---

## 🏗️ Struktur Kode

```
sistem-wilayah-indonesia/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point aplikasi
│   ├── models/
│   │   ├── __init__.py
│   │   └── wilayah.py          # Model data wilayah
│   ├── services/
│   │   ├── __init__.py
│   │   └── wilayah_service.py  # Logika bisnis
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py           # Endpoint API
│   └── utils/
│       ├── __init__.py
│       └── helpers.py          # Fungsi utilitas
├── data/
│   └── wilayah_data.json       # Data wilayah dalam format JSON
├── tests/
│   ├── __init__.py
│   ├── test_wilayah_service.py
│   └── test_api.py
├── docs/
│   └── api_documentation.md    # Dokumentasi API
├── requirements.txt            # Dependensi Python
├── README.md                   # Dokumentasi proyek
├── .gitignore                  # File yang diabaikan Git
└── run.py                      # Script untuk menjalankan aplikasi
```

---

## 🧪 Testing

Menjalankan unit test:
```bash
pip install pytest
pytest
```

---

## 📝 Changelog (Ringkasan)

Lihat `CHANGELOG.md` untuk detail lengkap. Ringkasan:
- **3.0.0 — 2025-11** (Pembaruan Terbaru)
  - Konversi ke RESTful API menggunakan FastAPI
  - Penambahan dokumentasi API otomatis
  - Unit testing dengan pytest
  - Struktur proyek modular
- **2.0.0 — 2025-08-19**
  - Complete rewrite; data komprehensif untuk 38 provinsi (416 kabupaten, 98 kota)
  - Advanced search, statistik, export JSON/TXT, CLI enhancements
- **1.0.0 — 2024-01-16**
  - Rilis awal: pencarian provinsi, listing, random trivia

---

## 🤝 Kontribusi

Silakan berkontribusi lewat:
1. Fork repository
2. Buat branch fitur: `git checkout -b feature/name`
3. Commit & push: `git commit -m "Deskripsi"` lalu `git push`
4. Buat Pull Request di GitHub

Label yang disarankan: `bug`, `enhancement`, `data-update`, `documentation`.

---

## 📊 Data Accuracy & Update Policy

- Data akurat per **Agustus 2025**.
- Major update: setiap 6 bulan. Minor update: bulanan. Verifikasi  tiap 2 minggu.
- Untuk laporan ketidaksesuaian  buat issue dengan label `data-update` dan sertakan sumber resmi.

---

## 📞 Kontak & Dukungan

- GitHub Issues: gunakan untuk bug/feature/data reports
- Email: sulucodes@gmail.com

---

## 📜 Lisensi

Kode dilisensikan di bawah **MIT License** — lihat file `LICENSE`.
> Catatan: Data mengikuti lisensi sumber masing-masing (contoh: Wikipedia CC BY-SA).

---

## 🙌 Acknowledgments

- Kementerian Dalam Negeri RI (Kemendagri)
- Badan Pusat Statistik (BPS)
- Wikipedia contributors
- Python community
- FastAPI community

---

*Last Updated: November 2025 — Document Version: 3.0*