Program Python ini dibuat untuk mempraktikkan berbagai operasi dasar pada struktur data list. Program dimulai dengan membuat sebuah list bernama *A* yang berisi lima elemen angka, yaitu `[10, 20, 30, 40, 90]`.
 Setelah list dibuat, program melakukan beberapa operasi akses data, seperti menampilkan elemen ke-3, mengambil elemen ke-2 hingga ke-4, serta menampilkan elemen terakhir dari list.
 Tahap selanjutnya adalah mengubah elemen dalam list, dimulai dengan mengganti elemen ke-4 menjadi nilai baru yaitu `99`, kemudian mengubah rentang elemen mulai dari index ke-4 hingga elemen terakhir menjadi `[100, 200]`, sehingga terjadi pembaruan pada list A.

Setelah melakukan modifikasi pada list A, program juga menambahkan elemen ke list baru bernama *B*. List B diambil dari dua elemen pertama list A menggunakan teknik *slicing*. Selanjutnya list B ditambahkan beberapa elemen baru berupa sebuah string (`"Python"`) dan tiga angka (`60, 70, 80`). Program kemudian menggabungkan list B yang telah diperluas dengan list A untuk menghasilkan sebuah list gabungan baru.

sehinga ketika di run akan seperti ini:

![Hasil Latihan 1](https://github.com/adriansyahmukti-svg/labpy4/blob/main/lab.py4/hasil%20eksekusi%20latihan1.png)


Program ini dibuat untuk melakukan input dan pengolahan data nilai mahasiswa secara interaktif. Pengguna dapat memasukkan nama mahasiswa, NIM, serta nilai Tugas, UTS, dan UAS. Setelah data dimasukkan, program akan menghitung nilai akhir menggunakan rumus perhitungan yang telah ditentukan, yaitu:

30% dari nilai Tugas

35% dari nilai UTS

35% dari nilai UAS

Setiap data mahasiswa disimpan dalam sebuah list yang berisi dictionary, sehingga setiap mahasiswa memiliki struktur data yang lengkap dan mudah dikelola. Program juga menyediakan pilihan untuk menambahkan data lebih dari satu mahasiswa. Ketika pengguna memilih untuk berhenti, seluruh data yang telah diinput akan ditampilkan dalam bentuk tabel yang rapi, berisi nomor urut, nama, NIM, nilai Tugas, UTS, UAS, dan nilai akhir yang ditampilkan dengan dua angka di belakang koma.

![Hasil Latihan 1](https://github.com/adriansyahmukti-svg/labpy4/blob/main/lab.py4/hasil2.png)

flowchat dari program di atas

           ┌────────────────────────────┐
           │   Mulai Program            │
           └──────────────┬─────────────┘
                          ▼
            ┌──────────────────────────┐
            │ Inisialisasi list kosong │
            │   data_mahasiswa = []    │
            └──────────────┬───────────┘
                           ▼
                ┌──────────────────┐
                │ Input Nama       │
                ├──────────────────┤
                │ Input NIM        │
                ├──────────────────┤
                │ Input Nilai      │
                │ Tugas, UTS, UAS  │
                └──────────┬───────┘
                           ▼
          ┌───────────────────────────────────┐
          │ Hitung nilai_akhir =              │
          │ (tugas*0.30) + (uts*0.35) + (uas*0.35) │
          └──────────────────┬────────────────┘
                             ▼
          ┌──────────────────────────────────┐
          │ Simpan data ke list              │
          │ data_mahasiswa.append({...})     │
          └──────────────────┬───────────────┘
                             ▼
             ┌────────────────────────────┐
             │ Tambah data lagi? (y/t)   │
             └───────┬───────────────────┘
                     │
          ┌──────────┴──────────┐
          │ y (ya)              │ t (tidak)
          ▼                     ▼
   ┌──────────────┐      ┌─────────────────────────┐
   │ Kembali ke    │      │ Tampilkan seluruh data  │
   │ input data    │      │ dalam bentuk tabel      │
   └──────────────┘      └───────────────┬─────────┘
                                         ▼
                             ┌──────────────────────┐
                             │      Selesai         │
                             └──────────────────────┘

lalu upload semua file ke github melalui terminal dengan cara!

buat terlebih dahulu folder project di komputer, lalu buka terminal di dalam folder tersebut. Inisialisasi Git dengan perintah git init, kemudian tambahkan file yang ingin diunggah menggunakan git add .. Setelah itu, simpan perubahan dengan git commit -m "pesan commit".

Selanjutnya hubungkan folder lokal dengan repository GitHub menggunakan perintah:
git remote add origin https://github.com/adriansyahmukti-svg/lab.py4.git
git push -u origin main

Setelah proses selesai, file akan muncul dan tersimpan di repository GitHub kamu.

