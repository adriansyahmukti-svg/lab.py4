data_mahasiswa = []

while True:
    print("\n=== Input Data Mahasiswa ===")
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("masukan nim mahasiswa:")
    tugas = float(input("Masukkan nilai Tugas (30%): "))
    uts = float(input("Masukkan nilai UTS (35%): "))
    uas = float(input("Masukkan nilai UAS (35%): "))

    
    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    
    data_mahasiswa.append({
        "nama": nama,
        "nim" : nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    })

    tambah = input("Tambah data lagi? (y/t): ").lower()
    if tambah == 't':
        break

print("\n=== Daftar Nilai Mahasiswa ===")
print("No | Nama\t| nim\t| Tugas\t| UTS\t| UAS\t| Nilai Akhir")
print("----------------------------------------------------------")
for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"{i}  | {mhs['nama']}\t|{mhs['nim']}\t| {mhs['tugas']}\t| {mhs['uts']}\t| {mhs['uas']}\t| {mhs['nilai_akhir']:.2f}")
