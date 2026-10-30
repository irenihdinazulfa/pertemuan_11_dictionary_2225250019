
# Latihan 2: Sistem Data Mahasiswa

# Fungsi untuk mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(data, nim):
    return data.get(nim, "Data tidak ditemukan")


# Fungsi untuk menghitung rata-rata nilai
def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = sum(mhs["nilai"] for mhs in data.values())
    return total / len(data)


# Data awal 5 mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

# 1. Mencari mahasiswa dengan NIM yang ada
print("=== PENCARIAN MAHASISWA ===")
print(cari_mahasiswa(data_mahasiswa, "A001"))

# 2. Mencari mahasiswa dengan NIM yang tidak ada
print(cari_mahasiswa(data_mahasiswa, "A010"))

# 3. Menambahkan mahasiswa baru
print("\n=== TAMBAH MAHASISWA ===")
data_mahasiswa["A006"] = {
    "nama": "Fina",
    "kelas": "B",
    "nilai": 90
}
print("Mahasiswa baru berhasil ditambahkan")
print(data_mahasiswa["A006"])

# 4. Mengubah nilai salah satu mahasiswa
print("\n=== UBAH NILAI MAHASISWA ===")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai Budi berhasil diubah")
print(data_mahasiswa["A002"])

# 5. Menampilkan seluruh data mahasiswa
print("\n=== REKAP DATA MAHASISWA ===")
for nim, mahasiswa in data_mahasiswa.items():
    print("NIM   :", nim)
    print("Nama  :", mahasiswa["nama"])
    print("Kelas :", mahasiswa["kelas"])
    print("Nilai :", mahasiswa["nilai"])
    print("------------------------")

# 6. Menghitung rata-rata nilai
print("\n=== RATA-RATA NILAI KELAS ===")
rata_rata = rata_rata_nilai(data_mahasiswa)
print(f"Rata-rata nilai: {rata_rata:.2f}")
