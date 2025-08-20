# Changelog

Semua perubahan penting pada proyek ini akan didokumentasikan dalam file ini.

Format ini berdasarkan [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
dan proyek ini mematuhi [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Ditambahkan
- RESTful API menggunakan framework FastAPI
- Dokumentasi API otomatis dengan Swagger/OpenAPI
- Unit test yang komprehensif dengan pytest
- Dokumentasi proyek dalam `README.md`
- Dokumentasi API dalam `docs/api_documentation.md`
- File `.gitignore` yang tepat untuk proyek Python
- Struktur direktori proyek yang terorganisir

### Diubah
- Merefaktor logika inti ke dalam lapisan layanan
- Memisahkan data ke dalam file JSON eksternal
- Mengonversi aplikasi CLI menjadi web API
- Meningkatkan organisasi dan modularitas kode

## [2.0.0] - 2025-08-19

### Ditambahkan
- 🎉 Penulisan ulang lengkap dengan data kabupaten/kota yang komprehensif
- 📊 Data lengkap untuk semua 38 provinsi di Indonesia
- 🗂️ 416 kabupaten dan 98 kota
- 🔍 Fungsi pencarian lanjutan untuk provinsi, kabupaten, dan kota
- 📈 Fitur statistik yang menunjukkan data administratif lengkap
- 💾 Fungsi ekspor ke format JSON dan TXT
- 🎨 Antarmuka CLI yang ditingkatkan dengan emoji dan pemformatan yang lebih baik
- 📚 Dokumentasi dan README yang komprehensif
- 🔧 Struktur proyek profesional dengan semua file pendukung

### Diubah
- ✨ Kemampuan pencarian fuzzy untuk input yang fleksibel
- 🔄 Pendekatan pemrograman berorientasi objek
- 📝 Petunjuk tipe untuk pemeliharaan kode yang lebih baik
- ⚡ Penanganan kesalahan dan umpan balik pengguna yang ditingkatkan
- 🎯 Pengalaman pengguna yang lebih baik dengan perintah yang intuitif

### Peningkatan Teknis
- 🏗️ Arsitektur berbasis kelas dengan `SistemWilayahIndonesia`
- 🔍 Metode terpisah untuk berbagai jenis pencarian
- 📁 Organisasi file dan struktur proyek yang tepat
- 🧪 Dokumentasi dan komentar kode yang lebih baik

## [1.0.0] - 2024-01-16

### Ditambahkan
- 🏛️ Pencarian provinsi dan ibu kota dasar
- 🎲 Fitur informasi provinsi acak
- 💻 Antarmuka command-line sederhana
- 📋 Fungsi daftar provinsi dasar

### Fitur
- 🔍 Pencarian provinsi berdasarkan nama
- 🎯 Informasi ibu kota
- 📜 Daftar semua provinsi
- 🎪 Trivia provinsi acak

### Cakupan Data
- 🗺️ 38 provinsi dengan ibu kota
- 🏢 Informasi administratif dasar

## Riwayat Pembaruan Data

### Agustus 2025
- ✅ Memperbarui semua data provinsi ke standar 2024
- ✅ Menambahkan provinsi baru: Papua Tengah, Papua Pegunungan, Papua Selatan, Papua Barat Daya
- ✅ Memverifikasi data kabupaten/kota dengan regulasi pemerintah terbaru
- ✅ Merujuk silang dengan sumber BPS dan Wikipedia

### Catatan Akurasi Data
- 📊 Total Provinsi: 38 (termasuk provinsi Papua terbaru)
- 🏛️ Total Kabupaten: 416
- 🏙️ Total Kota: 98
- 📍 Total Wilayah Administratif Tingkat 2: 514

## Pengakuan

### Sumber Data
- 🏛️ Kementerian Dalam Negeri Republik Indonesia
- 📊 Badan Pusat Statistik Indonesia
- 🌐 Kontributor Wikipedia

### Teknologi
- 🐍 Python 3.7+
- 📝 Library bawaan: `json`, `random`, `typing`, `datetime`
- 🎨 CLI dengan dukungan emoji

### Terima Kasih Khusus
- 🙏 Pemerintah Indonesia atas penyediaan data administratif terbuka
- 👥 Komunitas open source untuk alat dan inspirasi
- 📖 Editor Wikipedia untuk menjaga data wilayah yang akurat
- 🇮🇩 Indonesia sebagai kepulauan luar biasa untuk didokumentasikan

## Pembaruan Terbaru (November 2025)

### Ditambahkan
- ✨ Konversi proyek menjadi API RESTful menggunakan FastAPI
- 🌐 Endpoint API untuk semua fitur utama sistem
- 📖 Dokumentasi API lengkap dengan contoh penggunaan
- 🧪 Test suite untuk memastikan kualitas kode
- 📁 Struktur proyek yang modular dan terorganisir
- 🔧 Konfigurasi deployment yang siap produksi

### Ditingkatkan
- ⚡ Performa aplikasi dengan pemisahan concern
- 🛡️ Penanganan error yang lebih robust
- 📝 Validasi data dengan Pydantic models
- 🎨 Dokumentasi teknis yang komprehensif
- 🔍 Pencarian dan filtering yang dioptimalkan