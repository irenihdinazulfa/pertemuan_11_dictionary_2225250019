
# Pertemuan 11 - Dictionary/Map

Nama: Iren Ihdina Zulfa
NIM: 2225250019
Kelas: 3E

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Program menggunakan dictionary dengan NIM sebagai key utama.

Setiap NIM memiliki value berupa dictionary yang berisi:
- nama: Nama mahasiswa
- kelas: Kelas mahasiswa
- nilai: Nilai mahasiswa

Contoh:
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78}
}

## Cara Menjalankan
Buka terminal VS Code, kemudian jalankan:

python3 praktik/data_mahasiswa.py

## Test Case

| Input/Aksi | Hasil Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| Cari NIM A001 | Data Ayu tampil | Data Ayu tampil | Berhasil |
| Cari NIM A010 | Data tidak ditemukan | Data tidak ditemukan | Berhasil |
| Tambah A006 | Data Fina ditambahkan | Data Fina ditambahkan | Berhasil |
| Ubah nilai A002 | Nilai menjadi 82 | Nilai menjadi 82 | Berhasil |
| Tampilkan semua data | 6 mahasiswa tampil | 6 mahasiswa tampil | Berhasil |
| Hitung rata-rata | 85,17 | 85,17 | Berhasil |

## Refleksi
Kesalahan yang dapat terjadi adalah KeyError ketika mengakses
NIM yang tidak tersedia dalam dictionary.

Contohnya menggunakan data_mahasiswa["A010"],
padahal NIM tersebut tidak ada.

Cara memperbaikinya adalah menggunakan metode .get()
agar program menampilkan "Data tidak ditemukan"
tanpa menyebabkan error.
