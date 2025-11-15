A = [10, 20, 30, 40, 90]
print("List A awal:", A)

print("\n=== akses list ===")
print("Elemen ke-3:", A[2])
print("Elemen ke-2 sampai ke-4:", A[1:4])
print("Elemen terakhir:", A[-1])

print("\n=== ubah elemen list ===")
A[3] = 99
print("Setelah ubah elemen ke-4:", A)
A[3:] = [100, 200]
print("Setelah ubah elemen ke-4 sampai terakhir:", A)

print("\n=== tamah elemen list ===")
B = A[:2]
print("List B hasil salinan 2 bagian pertama:", B)
B += ["Python", 60, 70, 80] 
print("Setelah tambah string dan 3 nilai:", B)

gabungan = B + A
print("Gabungan list B dan list A:", gabungan)
