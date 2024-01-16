from random import choice as c

# Dictionary berisi nama provinsi dan ibu kota/kota kecil/kabupaten di Indonesia
provinsi = {
    "Nanggroe Aceh Darussalam": "Banda Aceh",
    "Sumatera Utara": "Medan",
    "Sumatera Selatan": "Palembang",
    "Sumatera Barat": "Padang",
    "Bengkulu": "Bengkulu",
    "Riau": "Pekanbaru",
    "Kepulauan Riau": "Tanjung Pinang",
    "Jambi": "Jambi",
    "Lampung": "Bandar Lampung",
    "Bangka Belitung": "Pangkal Pinang",
    "Kalimantan Barat": "Pontianak",
    "Kalimantan Timur": "Samarinda",
    "Kalimantan Selatan": "Banjarbaru",
    "Kalimantan Tengah": "Palangkaraya",
    "Kalimantan Utara": "Tanjung Selor",
    "Banten": "Serang",
    "DKI Jakarta": "Jakarta",
    "Jawa Barat": "Bandung",
    "Jawa Tengah": "Semarang",
    "Daerah Istimewa Yogyakarta": "Yogyakarta",
    "Jawa Timur": "Surabaya",
    "Bali": "Denpasar",
    "Nusa Tenggara Timur": "Kupang",
    "Nusa Tenggara Barat": "Mataram",
    "Gorontalo": "Gorontalo",
    "Sulawesi Barat": "Mamuju",
    "Sulawesi Tengah": "Palu",
    "Sulawesi Utara": "Manado",
    "Sulawesi Tenggara": "Kendari",
    "Sulawesi Selatan": "Makassar",
    "Maluku Utara": "Sofifi",
    "Maluku": "Ambon",
    "Papua Barat": "Manokwari",
    "Papua": "Jayapura",
    "Papua Tengah": "Nabire",
    "Papua Pegunungan": "Jayawijaya",
    "Papua Selatan": "Merauke",
    "Papua Barat Daya": "Sorong",
}

# Input nama provinsi dari pengguna
input_provinsi = input("Masukkan nama provinsi: ").title()

# Dapatkan ibu kota provinsi, jika tidak ada, berikan nama kota kecil/kabupaten
ibu_kota_provinsi = provinsi.get(input_provinsi, f"[pencarian...]\nMaaf, {input_provinsi} tidak ada dalam database")

# Tampilkan hasil ibu kota provinsi
print(f"Ibu kota {input_provinsi} adalah {ibu_kota_provinsi}.\n")

# Pilih provinsi acak beserta ibu kotanya
provinsi_random, ibu_kota_random = c(list(provinsi.items()))

# Pastikan provinsi acak berbeda dari input pengguna
while provinsi_random == input_provinsi:
    provinsi_random, ibu_kota_random = c(list(provinsi.items()))

# Tampilkan informasi provinsi acak
print("Dan, jika kamu penasaran,")
print(f"Ibu kota {provinsi_random} adalah {ibu_kota_random}.")
