"""
Sistem Informasi Wilayah Indonesia — Versi Refactor (2025)
==========================================================
Data Source: Permendagri No. 137/2017, BPS, Wikipedia (2024)
Author: Sulu Edward Julianto
Version: 3.0.1 - Fixed
Python: 3.10+
"""

from __future__ import annotations

import argparse
import json
import random
from typing import Dict, List, Tuple, Optional, Iterable
from datetime import datetime

DATA_VERSION = "2024-12"
DATA_SOURCE = "Kemendagri, BPS, Wikipedia (2024)"


def _norm(s: str) -> str:
    """Normalisasi string untuk pencarian yang lebih robust."""
    return " ".join(s.split()).strip().lower()


class SistemWilayahIndonesia:
    """Kelas untuk mengelola data wilayah administratif Indonesia."""

    def __init__(self):
        """Inisialisasi data wilayah Indonesia & struktur bantu."""
        self.data_wilayah: Dict[str, Dict[str, List[str] | str]] = {
            "Nanggroe Aceh Darussalam": {
                "ibu_kota": "Banda Aceh",
                "kabupaten": [
                    "Kabupaten Aceh Besar", "Kabupaten Aceh Barat", "Kabupaten Aceh Selatan",
                    "Kabupaten Aceh Timur", "Kabupaten Aceh Tengah", "Kabupaten Aceh Utara",
                    "Kabupaten Aceh Barat Daya", "Kabupaten Aceh Tenggara", "Kabupaten Aceh Tamiang",
                    "Kabupaten Aceh Jaya", "Kabupaten Aceh Singkil", "Kabupaten Bireuen",
                    "Kabupaten Gayo Lues", "Kabupaten Nagan Raya", "Kabupaten Pidie",
                    "Kabupaten Pidie Jaya", "Kabupaten Simeulue", "Kabupaten Bener Meriah"
                ],
                "kota": [
                    "Kota Banda Aceh", "Kota Langsa", "Kota Lhokseumawe", 
                    "Kota Sabang", "Kota Subulussalam"
                ]
            },
            "Sumatera Utara": {
                "ibu_kota": "Medan",
                "kabupaten": [
                    "Kabupaten Asahan", "Kabupaten Batubara", "Kabupaten Dairi", "Kabupaten Deli Serdang",
                    "Kabupaten Humbang Hasundutan", "Kabupaten Karo", "Kabupaten Labuhanbatu",
                    "Kabupaten Labuhanbatu Selatan", "Kabupaten Labuhanbatu Utara", "Kabupaten Langkat",
                    "Kabupaten Mandailing Natal", "Kabupaten Nias", "Kabupaten Nias Barat",
                    "Kabupaten Nias Selatan", "Kabupaten Nias Utara", "Kabupaten Padang Lawas",
                    "Kabupaten Padang Lawas Utara", "Kabupaten Pakpak Bharat", "Kabupaten Samosir",
                    "Kabupaten Serdang Bedagai", "Kabupaten Simalungun", "Kabupaten Tapanuli Selatan",
                    "Kabupaten Tapanuli Tengah", "Kabupaten Tapanuli Utara", "Kabupaten Toba"
                ],
                "kota": [
                    "Kota Medan", "Kota Binjai", "Kota Gunungsitoli", "Kota Padangsidimpuan",
                    "Kota Pematangsiantar", "Kota Sibolga", "Kota Tanjungbalai", "Kota Tebing Tinggi"
                ]
            },
            "Sumatera Barat": {
                "ibu_kota": "Padang",
                "kabupaten": [
                    "Kabupaten Agam", "Kabupaten Dharmasraya", "Kabupaten Kepulauan Mentawai",
                    "Kabupaten Lima Puluh Kota", "Kabupaten Padang Pariaman", "Kabupaten Pasaman",
                    "Kabupaten Pasaman Barat", "Kabupaten Pesisir Selatan", "Kabupaten Sijunjung",
                    "Kabupaten Solok", "Kabupaten Solok Selatan", "Kabupaten Tanah Datar"
                ],
                "kota": [
                    "Kota Padang", "Kota Bukittinggi", "Kota Padangpanjang", "Kota Pariaman",
                    "Kota Payakumbuh", "Kota Sawahlunto", "Kota Solok"
                ]
            },
            "Riau": {
                "ibu_kota": "Pekanbaru",
                "kabupaten": [
                    "Kabupaten Bengkalis", "Kabupaten Indragiri Hilir", "Kabupaten Indragiri Hulu",
                    "Kabupaten Kampar", "Kabupaten Kepulauan Meranti", "Kabupaten Kuantan Singingi",
                    "Kabupaten Pelalawan", "Kabupaten Rokan Hilir", "Kabupaten Rokan Hulu",
                    "Kabupaten Siak"
                ],
                "kota": ["Kota Pekanbaru", "Kota Dumai"]
            },
            "Jambi": {
                "ibu_kota": "Jambi",
                "kabupaten": [
                    "Kabupaten Batanghari", "Kabupaten Bungo", "Kabupaten Kerinci",
                    "Kabupaten Merangin", "Kabupaten Muaro Jambi", "Kabupaten Sarolangun",
                    "Kabupaten Tanjung Jabung Barat", "Kabupaten Tanjung Jabung Timur", "Kabupaten Tebo"
                ],
                "kota": ["Kota Jambi", "Kota Sungai Penuh"]
            },
            "Sumatera Selatan": {
                "ibu_kota": "Palembang",
                "kabupaten": [
                    "Kabupaten Banyuasin", "Kabupaten Empat Lawang", "Kabupaten Lahat",
                    "Kabupaten Muara Enim", "Kabupaten Musi Banyuasin", "Kabupaten Musi Rawas",
                    "Kabupaten Musi Rawas Utara", "Kabupaten Ogan Ilir", "Kabupaten Ogan Komering Ilir",
                    "Kabupaten Ogan Komering Ulu", "Kabupaten Ogan Komering Ulu Selatan",
                    "Kabupaten Ogan Komering Ulu Timur", "Kabupaten Penukal Abab Lematang Ilir"
                ],
                "kota": ["Kota Palembang", "Kota Lubuklinggau", "Kota Pagar Alam", "Kota Prabumulih"]
            },
            "Bengkulu": {
                "ibu_kota": "Bengkulu",
                "kabupaten": [
                    "Kabupaten Bengkulu Selatan", "Kabupaten Bengkulu Tengah", "Kabupaten Bengkulu Utara",
                    "Kabupaten Kaur", "Kabupaten Kepahiang", "Kabupaten Lebong",
                    "Kabupaten Mukomuko", "Kabupaten Rejang Lebong", "Kabupaten Seluma"
                ],
                "kota": ["Kota Bengkulu"]
            },
            "Lampung": {
                "ibu_kota": "Bandar Lampung",
                "kabupaten": [
                    "Kabupaten Lampung Barat", "Kabupaten Lampung Selatan", "Kabupaten Lampung Tengah",
                    "Kabupaten Lampung Timur", "Kabupaten Lampung Utara", "Kabupaten Mesuji",
                    "Kabupaten Pesawaran", "Kabupaten Pesisir Barat", "Kabupaten Pringsewu",
                    "Kabupaten Tanggamus", "Kabupaten Tulang Bawang", "Kabupaten Tulang Bawang Barat",
                    "Kabupaten Way Kanan"
                ],
                "kota": ["Kota Bandar Lampung", "Kota Metro"]
            },
            "Kepulauan Bangka Belitung": {
                "ibu_kota": "Pangkal Pinang",
                "kabupaten": [
                    "Kabupaten Bangka", "Kabupaten Bangka Barat", "Kabupaten Bangka Selatan",
                    "Kabupaten Bangka Tengah", "Kabupaten Belitung", "Kabupaten Belitung Timur"
                ],
                "kota": ["Kota Pangkal Pinang"]
            },
            "Kepulauan Riau": {
                "ibu_kota": "Tanjung Pinang",
                "kabupaten": [
                    "Kabupaten Bintan", "Kabupaten Karimun", "Kabupaten Kepulauan Anambas",
                    "Kabupaten Lingga", "Kabupaten Natuna"
                ],
                "kota": ["Kota Tanjung Pinang", "Kota Batam"]
            },
            "DKI Jakarta": {
                "ibu_kota": "Jakarta",
                "kabupaten": ["Kabupaten Administrasi Kepulauan Seribu"],
                "kota": [
                    "Kota Administrasi Jakarta Barat", "Kota Administrasi Jakarta Pusat",
                    "Kota Administrasi Jakarta Selatan", "Kota Administrasi Jakarta Timur",
                    "Kota Administrasi Jakarta Utara"
                ]
            },
            "Jawa Barat": {
                "ibu_kota": "Bandung",
                "kabupaten": [
                    "Kabupaten Bandung", "Kabupaten Bandung Barat", "Kabupaten Bekasi",
                    "Kabupaten Bogor", "Kabupaten Ciamis", "Kabupaten Cianjur", "Kabupaten Cirebon",
                    "Kabupaten Garut", "Kabupaten Indramayu", "Kabupaten Karawang", "Kabupaten Kuningan",
                    "Kabupaten Majalengka", "Kabupaten Pangandaran", "Kabupaten Purwakarta",
                    "Kabupaten Subang", "Kabupaten Sukabumi", "Kabupaten Sumedang", "Kabupaten Tasikmalaya"
                ],
                "kota": [
                    "Kota Bandung", "Kota Bekasi", "Kota Bogor", "Kota Cimahi", "Kota Cirebon",
                    "Kota Depok", "Kota Sukabumi", "Kota Tasikmalaya", "Kota Banjar"
                ]
            },
            "Jawa Tengah": {
                "ibu_kota": "Semarang",
                "kabupaten": [
                    "Kabupaten Banjarnegara", "Kabupaten Banyumas", "Kabupaten Batang",
                    "Kabupaten Blora", "Kabupaten Boyolali", "Kabupaten Brebes", "Kabupaten Cilacap",
                    "Kabupaten Demak", "Kabupaten Grobogan", "Kabupaten Jepara", "Kabupaten Karanganyar",
                    "Kabupaten Kebumen", "Kabupaten Kendal", "Kabupaten Klaten", "Kabupaten Kudus",
                    "Kabupaten Magelang", "Kabupaten Pati", "Kabupaten Pekalongan", "Kabupaten Pemalang",
                    "Kabupaten Purbalingga", "Kabupaten Purworejo", "Kabupaten Rembang",
                    "Kabupaten Semarang", "Kabupaten Sragen", "Kabupaten Sukoharjo", "Kabupaten Tegal",
                    "Kabupaten Temanggung", "Kabupaten Wonogiri", "Kabupaten Wonosobo"
                ],
                "kota": [
                    "Kota Semarang", "Kota Magelang", "Kota Pekalongan", "Kota Salatiga",
                    "Kota Surakarta", "Kota Tegal"
                ]
            },
            "Daerah Istimewa Yogyakarta": {
                "ibu_kota": "Yogyakarta",
                "kabupaten": [
                    "Kabupaten Bantul", "Kabupaten Gunungkidul", "Kabupaten Kulon Progo", "Kabupaten Sleman"
                ],
                "kota": ["Kota Yogyakarta"]
            },
            "Jawa Timur": {
                "ibu_kota": "Surabaya",
                "kabupaten": [
                    "Kabupaten Bangkalan", "Kabupaten Banyuwangi", "Kabupaten Blitar",
                    "Kabupaten Bojonegoro", "Kabupaten Bondowoso", "Kabupaten Gresik", "Kabupaten Jember",
                    "Kabupaten Jombang", "Kabupaten Kediri", "Kabupaten Lamongan", "Kabupaten Lumajang",
                    "Kabupaten Madiun", "Kabupaten Magetan", "Kabupaten Malang", "Kabupaten Mojokerto",
                    "Kabupaten Nganjuk", "Kabupaten Ngawi", "Kabupaten Pacitan", "Kabupaten Pamekasan",
                    "Kabupaten Pasuruan", "Kabupaten Ponorogo", "Kabupaten Probolinggo",
                    "Kabupaten Sampang", "Kabupaten Sidoarjo", "Kabupaten Situbondo", "Kabupaten Sumenep",
                    "Kabupaten Trenggalek", "Kabupaten Tuban", "Kabupaten Tulungagung"
                ],
                "kota": [
                    "Kota Surabaya", "Kota Batu", "Kota Blitar", "Kota Kediri", "Kota Madiun",
                    "Kota Malang", "Kota Mojokerto", "Kota Pasuruan", "Kota Probolinggo"
                ]
            },
            "Banten": {
                "ibu_kota": "Serang",
                "kabupaten": [
                    "Kabupaten Lebak", "Kabupaten Pandeglang", "Kabupaten Serang", "Kabupaten Tangerang"
                ],
                "kota": [
                    "Kota Serang", "Kota Cilegon", "Kota Tangerang", "Kota Tangerang Selatan"
                ]
            },
            "Bali": {
                "ibu_kota": "Denpasar",
                "kabupaten": [
                    "Kabupaten Badung", "Kabupaten Bangli", "Kabupaten Buleleng", "Kabupaten Gianyar",
                    "Kabupaten Jembrana", "Kabupaten Karangasem", "Kabupaten Klungkung", "Kabupaten Tabanan"
                ],
                "kota": ["Kota Denpasar"]
            },
            "Nusa Tenggara Barat": {
                "ibu_kota": "Mataram",
                "kabupaten": [
                    "Kabupaten Bima", "Kabupaten Dompu", "Kabupaten Lombok Barat", "Kabupaten Lombok Tengah",
                    "Kabupaten Lombok Timur", "Kabupaten Lombok Utara", "Kabupaten Sumbawa",
                    "Kabupaten Sumbawa Barat"
                ],
                "kota": ["Kota Mataram", "Kota Bima"]
            },
            "Nusa Tenggara Timur": {
                "ibu_kota": "Kupang",
                "kabupaten": [
                    "Kabupaten Alor", "Kabupaten Belu", "Kabupaten Ende", "Kabupaten Flores Timur",
                    "Kabupaten Kupang", "Kabupaten Lembata", "Kabupaten Manggarai", "Kabupaten Manggarai Barat",
                    "Kabupaten Manggarai Timur", "Kabupaten Nagekeo", "Kabupaten Ngada", "Kabupaten Rote Ndao",
                    "Kabupaten Sabu Raijua", "Kabupaten Sikka", "Kabupaten Sumba Barat", "Kabupaten Sumba Barat Daya",
                    "Kabupaten Sumba Tengah", "Kabupaten Sumba Timur", "Kabupaten Timor Tengah Selatan",
                    "Kabupaten Timor Tengah Utara", "Kabupaten Malaka"
                ],
                "kota": ["Kota Kupang"]
            },
            "Kalimantan Barat": {
                "ibu_kota": "Pontianak",
                "kabupaten": [
                    "Kabupaten Bengkayang", "Kabupaten Kapuas Hulu", "Kabupaten Kayong Utara",
                    "Kabupaten Ketapang", "Kabupaten Kubu Raya", "Kabupaten Landak", "Kabupaten Melawi",
                    "Kabupaten Mempawah", "Kabupaten Sambas", "Kabupaten Sanggau", "Kabupaten Sekadau",
                    "Kabupaten Sintang"
                ],
                "kota": ["Kota Pontianak", "Kota Singkawang"]
            },
            "Kalimantan Tengah": {
                "ibu_kota": "Palangkaraya",
                "kabupaten": [
                    "Kabupaten Barito Selatan", "Kabupaten Barito Timur", "Kabupaten Barito Utara",
                    "Kabupaten Gunung Mas", "Kabupaten Kapuas", "Kabupaten Katingan", "Kabupaten Kotawaringin Barat",
                    "Kabupaten Kotawaringin Timur", "Kabupaten Lamandau", "Kabupaten Murung Raya",
                    "Kabupaten Pulang Pisau", "Kabupaten Sukamara", "Kabupaten Seruyan"
                ],
                "kota": ["Kota Palangkaraya"]
            },
            "Kalimantan Selatan": {
                "ibu_kota": "Banjarmasin",
                "kabupaten": [
                    "Kabupaten Balangan", "Kabupaten Banjar", "Kabupaten Barito Kuala", "Kabupaten Hulu Sungai Selatan",
                    "Kabupaten Hulu Sungai Tengah", "Kabupaten Hulu Sungai Utara", "Kabupaten Kotabaru",
                    "Kabupaten Tabalong", "Kabupaten Tanah Bumbu", "Kabupaten Tanah Laut", "Kabupaten Tapin"
                ],
                "kota": ["Kota Banjarmasin", "Kota Banjarbaru"]
            },
            "Kalimantan Timur": {
                "ibu_kota": "Samarinda",
                "kabupaten": [
                    "Kabupaten Berau", "Kabupaten Kutai Barat", "Kabupaten Kutai Kartanegara",
                    "Kabupaten Kutai Timur", "Kabupaten Mahakam Ulu", "Kabupaten Paser", "Kabupaten Penajam Paser Utara"
                ],
                "kota": ["Kota Samarinda", "Kota Balikpapan", "Kota Bontang"]
            },
            "Kalimantan Utara": {
                "ibu_kota": "Tanjung Selor",
                "kabupaten": [
                    "Kabupaten Bulungan", "Kabupaten Malinau", "Kabupaten Nunukan", "Kabupaten Tana Tidung"
                ],
                "kota": ["Kota Tarakan"]
            },
            "Sulawesi Utara": {
                "ibu_kota": "Manado",
                "kabupaten": [
                    "Kabupaten Bolaang Mongondow", "Kabupaten Bolaang Mongondow Selatan",
                    "Kabupaten Bolaang Mongondow Timur", "Kabupaten Bolaang Mongondow Utara",
                    "Kabupaten Kepulauan Sangihe", "Kabupaten Kepulauan Siau Tagulandang Biaro",
                    "Kabupaten Kepulauan Talaud", "Kabupaten Minahasa", "Kabupaten Minahasa Selatan",
                    "Kabupaten Minahasa Tenggara", "Kabupaten Minahasa Utara"
                ],
                "kota": ["Kota Manado", "Kota Bitung", "Kota Kotamobagu", "Kota Tomohon"]
            },
            "Sulawesi Tengah": {
                "ibu_kota": "Palu",
                "kabupaten": [
                    "Kabupaten Banggai", "Kabupaten Banggai Kepulauan", "Kabupaten Banggai Laut",
                    "Kabupaten Buol", "Kabupaten Donggala", "Kabupaten Morowali", "Kabupaten Morowali Utara",
                    "Kabupaten Parigi Moutong", "Kabupaten Poso", "Kabupaten Sigi", "Kabupaten Tojo Una-Una",
                    "Kabupaten Tolitoli"
                ],
                "kota": ["Kota Palu"]
            },
            "Sulawesi Selatan": {
                "ibu_kota": "Makassar",
                "kabupaten": [
                    "Kabupaten Bantaeng", "Kabupaten Barru", "Kabupaten Bone", "Kabupaten Bulukumba",
                    "Kabupaten Enrekang", "Kabupaten Gowa", "Kabupaten Jeneponto", "Kabupaten Kepulauan Selayar",
                    "Kabupaten Luwu", "Kabupaten Luwu Timur", "Kabupaten Luwu Utara", "Kabupaten Maros",
                    "Kabupaten Pangkajene dan Kepulauan", "Kabupaten Pinrang", "Kabupaten Sidenreng Rappang",
                    "Kabupaten Sinjai", "Kabupaten Soppeng", "Kabupaten Takalar", "Kabupaten Tana Toraja",
                    "Kabupaten Toraja Utara", "Kabupaten Wajo"
                ],
                "kota": ["Kota Makassar", "Kota Palopo", "Kota Parepare"]
            },
            "Sulawesi Tenggara": {
                "ibu_kota": "Kendari",
                "kabupaten": [
                    "Kabupaten Bombana", "Kabupaten Buton", "Kabupaten Buton Selatan", "Kabupaten Buton Tengah",
                    "Kabupaten Buton Utara", "Kabupaten Kolaka", "Kabupaten Kolaka Timur", "Kabupaten Kolaka Utara",
                    "Kabupaten Konawe", "Kabupaten Konawe Kepulauan", "Kabupaten Konawe Selatan",
                    "Kabupaten Konawe Utara", "Kabupaten Muna", "Kabupaten Muna Barat", "Kabupaten Wakatobi"
                ],
                "kota": ["Kota Kendari", "Kota Bau-Bau"]
            },
            "Gorontalo": {
                "ibu_kota": "Gorontalo",
                "kabupaten": [
                    "Kabupaten Boalemo", "Kabupaten Bone Bolango", "Kabupaten Gorontalo",
                    "Kabupaten Gorontalo Utara", "Kabupaten Pohuwato"
                ],
                "kota": ["Kota Gorontalo"]
            },
            "Sulawesi Barat": {
                "ibu_kota": "Mamuju",
                "kabupaten": [
                    "Kabupaten Majene", "Kabupaten Mamasa", "Kabupaten Mamuju", "Kabupaten Mamuju Tengah",
                    "Kabupaten Mamuju Utara", "Kabupaten Polewali Mandar"
                ],
                "kota": []
            },
            "Maluku": {
                "ibu_kota": "Ambon",
                "kabupaten": [
                    "Kabupaten Buru", "Kabupaten Buru Selatan", "Kabupaten Kepulauan Aru",
                    "Kabupaten Maluku Barat Daya", "Kabupaten Maluku Tengah", "Kabupaten Maluku Tenggara",
                    "Kabupaten Maluku Tenggara Barat", "Kabupaten Seram Bagian Barat", "Kabupaten Seram Bagian Timur"
                ],
                "kota": ["Kota Ambon", "Kota Tual"]
            },
            "Maluku Utara": {
                "ibu_kota": "Sofifi",
                "kabupaten": [
                    "Kabupaten Halmahera Barat", "Kabupaten Halmahera Selatan", "Kabupaten Halmahera Tengah",
                    "Kabupaten Halmahera Timur", "Kabupaten Halmahera Utara", "Kabupaten Kepulauan Sula",
                    "Kabupaten Pulau Morotai", "Kabupaten Pulau Taliabu"
                ],
                "kota": ["Kota Ternate", "Kota Tidore Kepulauan"]
            },
            "Papua": {
                "ibu_kota": "Jayapura",
                "kabupaten": [
                    "Kabupaten Biak Numfor", "Kabupaten Jayapura", "Kabupaten Keerom", "Kabupaten Mamberamo Raya",
                    "Kabupaten Sarmi", "Kabupaten Supiori", "Kabupaten Waropen", "Kabupaten Yapen Kepulauan"
                ],
                "kota": ["Kota Jayapura"]
            },
            "Papua Barat": {
                "ibu_kota": "Manokwari",
                "kabupaten": [
                    "Kabupaten Fakfak", "Kabupaten Kaimana", "Kabupaten Manokwari", "Kabupaten Manokwari Selatan",
                    "Kabupaten Pegunungan Arfak", "Kabupaten Raja Ampat", "Kabupaten Teluk Bintuni"
                ],
                "kota": []
            },
            "Papua Selatan": {
                "ibu_kota": "Merauke",
                "kabupaten": [
                    "Kabupaten Asmat", "Kabupaten Boven Digoel", "Kabupaten Mappi", "Kabupaten Merauke"
                ],
                "kota": []
            },
            "Papua Tengah": {
                "ibu_kota": "Nabire",
                "kabupaten": [
                    "Kabupaten Deiyai", "Kabupaten Dogiyai", "Kabupaten Intan Jaya", "Kabupaten Mimika",
                    "Kabupaten Nabire", "Kabupaten Paniai", "Kabupaten Puncak", "Kabupaten Puncak Jaya"
                ],
                "kota": []
            },
            "Papua Pegunungan": {
                "ibu_kota": "Jayawijaya",
                "kabupaten": [
                    "Kabupaten Jayawijaya", "Kabupaten Lanny Jaya", "Kabupaten Mamberamo Tengah",
                    "Kabupaten Nduga", "Kabupaten Pegunungan Bintang", "Kabupaten Tolikara",
                    "Kabupaten Yahukimo", "Kabupaten Yalimo"
                ],
                "kota": []
            },
            "Papua Barat Daya": {
                "ibu_kota": "Sorong",
                "kabupaten": [
                    "Kabupaten Maybrat", "Kabupaten Raja Ampat", "Kabupaten Sorong",
                    "Kabupaten Sorong Selatan", "Kabupaten Tambrauw"
                ],
                "kota": ["Kota Sorong"]
            },
        }

        self._calculate_stats()
        self._build_alias_map()

    # ------------------------------ Internal helpers ------------------------------
    def _calculate_stats(self) -> None:
        """Menghitung statistik data wilayah."""
        self.total_provinsi: int = len(self.data_wilayah)
        self.total_kabupaten: int = sum(len(d["kabupaten"]) for d in self.data_wilayah.values())
        self.total_kota: int = sum(len(d["kota"]) for d in self.data_wilayah.values())

    def _build_alias_map(self) -> None:
        """Membangun peta alias (nama lain) -> nama provinsi kanonik."""
        self._alias_map: Dict[str, str] = {}
        for prov in self.data_wilayah.keys():
            self._alias_map[_norm(prov)] = prov
        # Alias umum
        manual_alias = {
        # Aceh
        "aceh": "Nanggroe Aceh Darussalam",
        "nad": "Nanggroe Aceh Darussalam",

        # Sumatera Utara
        "sumut": "Sumatera Utara",

        # Sumatera Barat
        "sumbar": "Sumatera Barat",

        # Riau
        "riau": "Riau",

        # Kepulauan Riau
        "kepri": "Kepulauan Riau",

        # Jambi
        "jambi": "Jambi",

        # Sumatera Selatan
        "sumsel": "Sumatera Selatan",

        # Kep. Bangka Belitung
        "babel": "Kepulauan Bangka Belitung",

        # Bengkulu
        "bengkulu": "Bengkulu",

        # Lampung
        "lampung": "Lampung",

        # DKI Jakarta
        "jakarta": "DKI Jakarta",

        # Jawa Barat
        "jabar": "Jawa Barat",

        # Jawa Tengah
        "jateng": "Jawa Tengah",

        # DI Yogyakarta
        "diy": "Daerah Istimewa Yogyakarta",
        "yogyakarta": "Daerah Istimewa Yogyakarta",
        "jogja": "Daerah Istimewa Yogyakarta",

        # Jawa Timur
        "jatim": "Jawa Timur",

        # Banten
        "banten": "Banten",

        # Bali
        "bali": "Bali",

        # Nusa Tenggara Barat
        "ntb": "Nusa Tenggara Barat",

        # Nusa Tenggara Timur
        "ntt": "Nusa Tenggara Timur",

        # Kalimantan Barat
        "kalbar": "Kalimantan Barat",

        # Kalimantan Tengah
        "kalteng": "Kalimantan Tengah",

        # Kalimantan Selatan
        "kalsel": "Kalimantan Selatan",

        # Kalimantan Timur
        "kaltim": "Kalimantan Timur",

        # Kalimantan Utara
        "kaltara": "Kalimantan Utara",
        "kalut": "Kalimantan Utara",

        # Sulawesi Utara
        "sulut": "Sulawesi Utara",

        # Gorontalo
        "gorontalo": "Gorontalo",

        # Sulawesi Tengah
        "sulteng": "Sulawesi Tengah",

        # Sulawesi Barat
        "sulbar": "Sulawesi Barat",

        # Sulawesi Selatan
        "sulsel": "Sulawesi Selatan",

        # Sulawesi Tenggara
        "sultra": "Sulawesi Tenggara",

        # Maluku
        "maluku": "Maluku",

        # Maluku Utara
        "malut": "Maluku Utara",

        # Papua
        "papua": "Papua",

        # Papua Barat
        "papua barat": "Papua Barat",

        # Papua Barat Daya (DOB)
        "papua barat daya": "Papua Barat Daya",

        # Papua Tengah (DOB)
        "papua tengah": "Papua Tengah",

        # Papua Selatan (DOB)
        "papua selatan": "Papua Selatan",

        # Papua Pegunungan (DOB)
        "papua pegunungan": "Papua Pegunungan",
        }
        for k, v in manual_alias.items():
            self._alias_map[k] = v

    def _resolve_prov(self, nama_provinsi: str) -> Optional[str]:
        key = _norm(nama_provinsi)
        if key in self._alias_map:
            return self._alias_map[key]
        # fallback substring match
        for prov in self.data_wilayah.keys():
            if key in _norm(prov) or _norm(prov) in key:
                return prov
        return None

    # ------------------------------ Public API ------------------------------
    def cari_provinsi(self, nama_provinsi: str) -> Optional[Dict]:
        """Mencari informasi provinsi berdasarkan nama."""
        prov_name = self._resolve_prov(nama_provinsi)
        if not prov_name:
            return None
        data = self.data_wilayah[prov_name]
        return {
            "nama": prov_name,
            "ibu_kota": data["ibu_kota"],
            "kabupaten": list(data["kabupaten"]),
            "kota": list(data["kota"]),
            "total_kabupaten": len(data["kabupaten"]),
            "total_kota": len(data["kota"]),
        }

    def cari_kabupaten_kota(self, nama_wilayah: str) -> Optional[List[Dict]]:
        """Mencari kabupaten/kota di seluruh Indonesia (substring & case-insensitive)."""
        q = _norm(nama_wilayah)
        if not q:
            return None
        hasil: List[Dict] = []
        for provinsi, data in self.data_wilayah.items():
            for kab in data["kabupaten"]:
                nm = _norm(kab)
                if q in nm or nm in q:
                    hasil.append({
                        "nama": kab,
                        "jenis": "Kabupaten",
                        "provinsi": provinsi,
                        "ibu_kota_provinsi": data["ibu_kota"],
                    })
            for kota in data["kota"]:
                nm = _norm(kota)
                if q in nm or nm in q:
                    hasil.append({
                        "nama": kota,
                        "jenis": "Kota",
                        "provinsi": provinsi,
                        "ibu_kota_provinsi": data["ibu_kota"],
                    })
        return hasil or None

    def dapatkan_provinsi_acak(self, kecuali_provinsi: str | None = None) -> Dict:
        """Mendapatkan provinsi dan informasinya secara acak (opsional pengecualian)."""
        items = list(self.data_wilayah.items())
        if kecuali_provinsi:
            resolved = self._resolve_prov(kecuali_provinsi)
            if resolved:
                items = [it for it in items if it[0] != resolved]
        provinsi_terpilih = random.choice(items)
        return {
            "nama": provinsi_terpilih[0],
            **provinsi_terpilih[1],
            "total_kabupaten": len(provinsi_terpilih[1]["kabupaten"]),
            "total_kota": len(provinsi_terpilih[1]["kota"]),
        }

    def dapatkan_statistik(self) -> Dict[str, int]:
        """Mendapatkan statistik wilayah Indonesia."""
        return {
            "total_provinsi": self.total_provinsi,
            "total_kabupaten": self.total_kabupaten,
            "total_kota": self.total_kota,
            "total_wilayah": self.total_kabupaten + self.total_kota,
        }

    def export_data(self, format_file: str = "json", directory: Optional[str] = None) -> str:
        """Export seluruh data ke file JSON atau TXT.

        Args:
            format_file: "json" atau "txt" (default: json)
            directory: direktori tujuan (default: cwd)
        Returns:
            path file yang dibuat
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if directory is None:
            directory = "."
        if format_file.lower() == "json":
            filename = f"{directory}/data_wilayah_indonesia_{timestamp}.json"
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(self.data_wilayah, f, ensure_ascii=False, indent=2)
        else:
            filename = f"{directory}/data_wilayah_indonesia_{timestamp}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                for provinsi, data in self.data_wilayah.items():
                    f.write(f"PROVINSI: {provinsi}\n")
                    f.write(f"IBU KOTA: {data['ibu_kota']}\n")
                    f.write(f"KABUPATEN ({len(data['kabupaten'])}): {', '.join(data['kabupaten'])}\n")
                    f.write(f"KOTA ({len(data['kota'])}): {', '.join(data['kota'])}\n")
                    f.write("-" * 80 + "\n")
        return filename

    # ------------------------------ UI helpers ------------------------------
    def tampilkan_daftar_provinsi(self) -> None:
        """Menampilkan daftar semua provinsi ke stdout."""
        print("\n" + "=" * 60)
        print("           DAFTAR PROVINSI DI INDONESIA")
        print("=" * 60)
        for i, (provinsi, data) in enumerate(sorted(self.data_wilayah.items()), 1):
            kab_count = len(data["kabupaten"])
            kota_count = len(data["kota"])
            print(f"{i:2}. {provinsi:<35} | {data['ibu_kota']:<15}")
            print(f"    └─ {kab_count} Kabupaten, {kota_count} Kota")
        print("=" * 60)
        print(f"Total: {self.total_provinsi} Provinsi | {self.total_kabupaten} Kabupaten | {self.total_kota} Kota")


def tampilkan_header() -> None:
    """Menampilkan header aplikasi CLI."""
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 8 + "SISTEM INFORMASI WILAYAH INDONESIA" + " " * 16 + "║")
    print("║" + " " * 12 + "Provinsi & Kabupaten/Kota" + " " * 19 + "║")
    print("╠" + "═" * 58 + "╣")
    print("║ Perintah:                                               ║")
    print("║ • 'daftar'    - Lihat semua provinsi                    ║")
    print("║ • 'statistik' - Lihat statistik wilayah                 ║")
    print("║ • 'export'    - Export data ke file                     ║")
    print("║ • 'keluar' atau 'quit' - Keluar dari program            ║")
    print("╚" + "═" * 58 + "╝")


def run_interactive() -> None:
    """Mode interaktif via input() seperti versi asli."""
    sistem = SistemWilayahIndonesia()
    tampilkan_header()

    while True:
        try:
            print("\n" + "─" * 60)
            input_pengguna = input("🔍 Masukkan nama provinsi/kabupaten/kota: ").strip()
            if not input_pengguna:
                print("❌ Mohon masukkan input yang valid.")
                continue
            perintah = _norm(input_pengguna)

            if perintah in ["keluar", "quit", "exit"]:
                print("\n✅ Terima kasih telah menggunakan Sistem Informasi Wilayah Indonesia!")
                print(f"📊 Sumber data: {DATA_SOURCE}")
                break
            elif perintah == "daftar":
                sistem.tampilkan_daftar_provinsi()
                continue
            elif perintah == "statistik":
                stats = sistem.dapatkan_statistik()
                print("\n📊 STATISTIK WILAYAH INDONESIA")
                print("=" * 40)
                print(f"• Total Provinsi    : {stats['total_provinsi']}")
                print(f"• Total Kabupaten   : {stats['total_kabupaten']}")
                print(f"• Total Kota        : {stats['total_kota']}")
                print(f"• Total Wilayah     : {stats['total_wilayah']}")
                continue
            elif perintah == "export":
                format_export = input("Format file (json/txt): ").strip().lower()
                if format_export not in ("json", "txt"):
                    format_export = "json"
                filename = sistem.export_data(format_export)
                print(f"✅ Data berhasil di-export ke: {filename}")
                continue

            info_provinsi = sistem.cari_provinsi(input_pengguna)
            if info_provinsi:
                print(f"\n🏛️  PROVINSI: {info_provinsi['nama']}")
                print(f"🏢 Ibu Kota: {info_provinsi['ibu_kota']}")
                print(f"📊 Kabupaten: {info_provinsi['total_kabupaten']} | Kota: {info_provinsi['total_kota']}")

                if info_provinsi["kabupaten"]:
                    print(f"\n📍 KABUPATEN ({info_provinsi['total_kabupaten']}):")
                    for i, kab in enumerate(info_provinsi["kabupaten"], 1):
                        print(f"   {i:2}. {kab}")

                if info_provinsi["kota"]:
                    print(f"\n🏙️  KOTA ({info_provinsi['total_kota']}):")
                    for i, kota in enumerate(info_provinsi["kota"], 1):
                        print(f"   {i:2}. {kota}")

                prov_acak = sistem.dapatkan_provinsi_acak(input_pengguna)
                print("\n💡 Tahukah Anda?")
                print(
                    f"   Provinsi {prov_acak['nama']} memiliki ibu kota {prov_acak['ibu_kota']}\n"
                    f"   dengan {prov_acak['total_kabupaten']} kabupaten dan {prov_acak['total_kota']} kota."
                )
                continue

            hasil = sistem.cari_kabupaten_kota(input_pengguna)
            if hasil:
                print(f"\n🔍 Ditemukan {len(hasil)} hasil:")
                for i, w in enumerate(hasil, 1):
                    print(f"{i}. {w['nama']}")
                    print(f"   └─ {w['jenis']} di Provinsi {w['provinsi']}")
                    print(f"      (Ibu kota provinsi: {w['ibu_kota_provinsi']})")
                continue

            print(f"\n❌ '{input_pengguna}' tidak ditemukan dalam database.")
            print("💡 Tips: Ketik 'daftar' untuk melihat semua provinsi yang tersedia.")
        except KeyboardInterrupt:
            print("\n\n⚠️  Program dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"\n❌ Terjadi kesalahan: {e}")
            print("🔄 Silakan coba lagi.")


def main(argv: Optional[Iterable[str]] = None) -> None:
    """Entry point dengan argparse: bisa interaktif atau sekali jalan."""
    parser = argparse.ArgumentParser(description="Sistem Informasi Wilayah Indonesia")
    parser.add_argument("query", nargs="?", help="Nama provinsi/kabupaten/kota atau perintah: daftar/statistik/export")
    parser.add_argument("--format", dest="format", choices=["json", "txt"], default="json", help="Format export")
    parser.add_argument("--dir", dest="directory", default=".", help="Direktori export")
    parser.add_argument("--interactive", action="store_true", help="Jalankan mode interaktif")
    args = parser.parse_args(argv)

    if args.interactive or args.query is None:
        return run_interactive()

    sistem = SistemWilayahIndonesia()
    q = _norm(args.query)

    if q == "daftar":
        sistem.tampilkan_daftar_provinsi()
        return
    if q == "statistik":
        print(json.dumps(sistem.dapatkan_statistik(), ensure_ascii=False, indent=2))
        return
    if q == "export":
        path = sistem.export_data(args.format, args.directory)
        print(path)
        return

    info = sistem.cari_provinsi(args.query)
    if info:
        print(json.dumps(info, ensure_ascii=False, indent=2))
        return
    hasil = sistem.cari_kabupaten_kota(args.query)
    if hasil:
        print(json.dumps(hasil, ensure_ascii=False, indent=2))
        return
    print("Tidak ditemukan.")


if __name__ == "__main__":
    main()