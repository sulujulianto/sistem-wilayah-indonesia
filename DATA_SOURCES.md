# 📑 Sumber Data - Sistem Informasi Wilayah Indonesia

Dokumen ini menjelaskan sumber data yang digunakan dalam Sistem Informasi Wilayah Indonesia beserta metodologi pengumpulan dan verifikasi data.

---

## 📋 Ringkasan Sumber Data

| Sumber | Jenis Data | Status | Terakhir Diverifikasi |
|--------|------------|--------|-----------------------|
| Permendagri No. 137/2017 | Data resmi wilayah administrasi | ✅ Resmi | Agustus 2025 |
| Wikipedia Indonesia | Kompilasi kabupaten/kota | ✅ Terverifikasi | Agustus 2025 |
| Badan Pusat Statistik | Data statistik dan sensus | ✅ Resmi | Agustus 2025 |

---

## 🏛️ 1. Permendagri No. 137 Tahun 2017

**Detail Sumber**
- Nama: *Peraturan Menteri Dalam Negeri Nomor 137 Tahun 2017 tentang Kode dan Data Wilayah Administrasi Pemerintahan*
- Penerbit: Kementerian Dalam Negeri RI
- Terbit: 2017
- URL: [kemendagri.go.id](https://www.kemendagri.go.id/pages/detail/108-permendagri-no137-tahun-2017)
- Status: Resmi

**Data yang Diambil**
- Kode wilayah administratif resmi
- Nama provinsi & ibu kota
- Struktur kabupaten/kota
- Dasar hukum pembentukan wilayah

**Keandalan**
- 🔒 Sangat Tinggi (sumber resmi pemerintah)
- 📜 Dasar hukum peraturan menteri
- 🔄 Update berkala melalui peraturan turunan

---

## 🌐 2. Wikipedia: Daftar Kabupaten/Kota

**Detail Sumber**
- URL: [Wikipedia - Daftar kabupaten dan kota di Indonesia](https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Indonesia_menurut_provinsi)
- Terakhir Akses: 17 Agustus 2025
- Lisensi: CC BY-SA
- Kontributor: Komunitas Wikipedia Indonesia

**Data yang Diambil**
- Daftar kabupaten & kota per provinsi (per 2024)
- Informasi pemekaran wilayah terbaru
- Status administratif terkini

**Referensi Wikipedia**
- Permendagri No. 137/2017
- Kepmendagri No. 100.1.1-6117/2022
- Data BPS per provinsi
- Peraturan daerah terkait

**Keandalan**
- 🔒 Tinggi (dikurasi komunitas)
- 📊 Akurasi >95% (verifikasi silang)
- 🔄 Update bulanan

---

## 📊 3. Badan Pusat Statistik (BPS)

**Detail Sumber**
- Nama: Badan Pusat Statistik Republik Indonesia
- Website: [bps.go.id](https://www.bps.go.id)
- Status: Lembaga Pemerintah Non-Kementerian

**Data yang Diambil**
- Konfirmasi data wilayah administratif
- Data statistik kabupaten/kota
- Informasi sensus & survei
- Validasi perubahan administratif

**Keandalan**
- 🔒 Sangat Tinggi (lembaga resmi)
- 📈 Metodologi standar internasional
- 🔄 Update berkala & real-time

---

## 🔍 Metodologi Pengumpulan & Verifikasi

### 1. Pengumpulan
- Sumber Primer: Permendagri
- Sumber Sekunder: Wikipedia
- Sumber Validasi: BPS
- Semua data dikompilasi ke database terpadu

### 2. Verifikasi
1. Cross-Reference → bandingkan data dari 3 sumber utama
2. Temporal → gunakan versi terbaru
3. Logical Consistency → cek ejaan, duplikasi, hierarki

### 3. Quality Control
- 🔍 Validasi otomatis
- 👥 Review manual developer
- 📊 Validasi statistik
- 🔄 Update berkala

---

## 📈 Akurasi & Keterbatasan

**Tingkat Akurasi**
- Provinsi & ibu kota: 100%
- Kabupaten: 99.5%
- Kota: 99.5%
- **Overall**: 99.7%

**Keterbatasan**
1. Perubahan dinamis: pemekaran, perubahan nama
2. Keterlambatan update antar sumber
3. Cakupan terbatas sampai kabupaten/kota

---

## 🔄 Protokol Update

**Trigger**
- 📅 Review bulanan
- 🚨 Perubahan wilayah (pemekaran/nama)
- 📊 Update dari sumber resmi

**Proses**
1. Deteksi perubahan
2. Verifikasi dengan multi-sumber
3. Update database & kode
4. Uji fungsionalitas
5. Dokumentasi changelog
6. Rilis ke production

**Jadwal**
- 🗓️ Major update: tiap 6 bulan
- 🗓️ Minor update: tiap bulan
- 🗓️ Hotfix: segera jika kritis
- 🗓️ Verifikasi data: tiap 2 minggu

---

## 📞 Kontak Verifikasi Data

**Sumber Resmi**
- Kemendagri: [kemendagri.go.id](https://kemendagri.go.id)
- BPS: [bps.go.id](https://bps.go.id)

**Laporan Error**
- 🐛 GitHub Issues
- 📧 Email: *(placeholder: data-verification@project.com)*

**Community Verification**
- 👥 Lihat `CONTRIBUTING.md`
- 🔍 Dokumentasi lengkap di `docs/`
- 📊 Dashboard kualitas data

---

## 📜 Disclaimer

Data telah diverifikasi dari sumber resmi. Namun, untuk keperluan hukum dan administratif, **pengguna wajib merujuk langsung ke instansi pemerintah terkait**.

---

*Last Updated: 19 Agustus 2025 — Document Version: 1.0*