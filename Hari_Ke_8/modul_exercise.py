import numpy as np

data = []
jumlah_siswa = int(input("Masukan Jumlah Siswa : "))

print("="*100)

for i in range (0, jumlah_siswa):
    nilai = int(input(f'Masukan Nilai Mahasiswa Ke {i+1} : '))
    data.append(nilai)
    
print(f"Nilai Rata-Rata : {np.mean(data)}")
print(f"Nilai Tertinggi : {np.max(data)}")
print(f"Nilai Terendah : {np.min(data)}")
print(f"Jumlah Siswa Di Atas Rata-Rata : {np.sum(data >= np.mean(data))}")
print("="*100)