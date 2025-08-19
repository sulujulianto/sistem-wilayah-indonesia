# 🗺️ Sistem Informasi Wilayah Indonesia

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/)

Sistem informasi komprehensif untuk mencari data provinsi, ibu kota, kabupaten, dan kota di Indonesia — data update hingga Agustus 2025.

---

## 📋 Deskripsi

Program ini menyediakan akses mudah ke informasi administratif wilayah Indonesia, termasuk:
- **38 Provinsi** dengan ibu kotanya
- **416 Kabupaten**
- **98 Kota**
- Total **514** wilayah administratif tingkat kedua

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

### 🎨 Antarmuka
- CLI sederhana, interaktif, dan ramah pengguna
- Emoji & formatting untuk meningkatkan keterbacaan
- Penanganan error yang informatif

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
git clone https://github.com/username/Pencari-Ibu-Kota-Provinsi-Indonesia.git
cd Pencari-Ibu-Kota-Provinsi-Indonesia
python -m venv venv
# activate venv:
# macOS / Linux:
source venv/bin/activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python sistem_wilayah_indonesia.py
```

---

## 🚀 Penggunaan (CLI)

Saat program berjalan, Anda akan diminta memasukkan perintah atau kata kunci:
- `daftar` → tampilkan semua provinsi
- `statistik` → tampilkan statistik (total provinsi/kabupaten/kota)
- `export` → export data (pilih format JSON atau TXT)
- `keluar` → keluar aplikasi

Contoh interaksi:
```
🔍 Masukkan nama provinsi/kabupaten/kota: Jawa Barat

🏛️  PROVINSI: Jawa Barat
🏢 Ibu Kota: Bandung
📊 Kabupaten: 18 | Kota: 9
📍 Kabupaten: Kabupaten Bandung, Kabupaten Bandung Barat, Kabupaten Bekasi
   ... dan 15 kabupaten lainnya
🏙️  Kota: Kota Bandung, Kota Bekasi, Kota Bogor, Kota Cimahi, Kota Cirebon, Kota Depok, Kota Sukabumi, Kota Tasikmalaya, Kota Banjar
```

---

## 🏗️ Struktur Kode & API singkat

File utama: `sistem_wilayah_indonesia.py`

Kelas utama: `SistemWilayahIndonesia`
- `cari_provinsi(nama_provinsi: str) -> Optional[Dict]`  
- `cari_kabupaten_kota(nama_wilayah: str) -> Optional[List[Dict]]`  
- `dapatkan_provinsi_acak(kecuali_provinsi: str = None) -> Dict`  
- `dapatkan_statistik() -> Dict`  
- `export_data(format_file: str = "json") -> str`

Contoh pemakaian programatik:
```python
from sistem_wilayah_indonesia import SistemWilayahIndonesia

sistem = SistemWilayahIndonesia()
print(sistem.dapatkan_statistik())
print(sistem.cari_provinsi("Jawa Barat"))
```

---

## 🗂️ Struktur Repository

```
Pencari-Ibu-Kota-Provinsi-Indonesia/
├── sistem_wilayah_indonesia.py
├── requirements.txt
├── README.md
├── LICENSE
├── DATA_SOURCES.md
├── CHANGELOG.md
├── .gitignore
└── data_export/  # dibuat otomatis saat export
```

---

## 📝 Changelog (Ringkasan)

Lihat `CHANGELOG.md` untuk detail lengkap. Ringkasan:
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
- Major update: setiap 6 bulan. Minor update: bulanan. Verifikasi data: tiap 2 minggu.  
- Untuk laporan ketidaksesuaian data: buat issue dengan label `data-update` dan sertakan sumber resmi.

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

---

*Last Updated: 19 Agustus 2025 — Document Version: 1.0*