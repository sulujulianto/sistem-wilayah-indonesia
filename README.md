# Pencari Ibu Kota Provinsi Indonesia

Script Python ini memungkinkan pengguna untuk memasukkan nama provinsi di Indonesia dan menemukan ibu kota provinsi tersebut. Selain itu, script ini memberikan informasi mengenai sebuah provinsi acak beserta ibu kotanya untuk keingintahuan tambahan.

## Cara Menggunakan:

1. Jalankan script.
2. Masukkan nama provinsi Indonesia saat diminta.
3. Script akan menampilkan ibu kota provinsi yang dimasukkan.
4. Jika ingin tahu ibu kota provinsi acak lainnya, script akan memberikan informasi tersebut.

## Penjelasan Kode:

Script ini dimulai dengan mendefinisikan sebuah kamus (dictionary) bernama `provinsi` yang berisi nama provinsi di Indonesia sebagai kunci dan ibu kota masing-masing sebagai nilainya.

```python
from random import choice as c

provinsi = {
    # ... (daftar provinsi Indonesia dan ibu kotanya)
}

input_provinsi = input("Masukkan nama provinsi: ").title()

ibu_kota_provinsi = provinsi.get(input_provinsi, f"[pencarian...]\nMaaf, {input_provinsi} tidak ada dalam database")

print(f"Ibu kota {input_provinsi} adalah {ibu_kota_provinsi}.\n")

provinsi_random, ibu_kota_random = c(list(provinsi.items()))

while provinsi_random == input_provinsi:
    provinsi_random, ibu_kota_random = c(list(provinsi.items()))

print("Dan, jika kamu penasaran,")
print(f"Ibu kota {provinsi_random} adalah {ibu_kota_random}.")
