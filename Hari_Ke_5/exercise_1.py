kelas = str(input('Masukan Kelas: ')).upper()
jumlah = int(input('Masukan Jumlah Mahasiswa:'))
total = 0

for i in range (0, jumlah+1):
    nilai = int(input(f'Masukan Nilai Mahasiswa Ke {i} : '))
    total += nilai
    rata_rata = total / jumlah

print("="*30)

print(f'Kelas : {kelas}')
print(f'Jumlah Mahasiswa : {jumlah}')
print(f'Nilai Rata-Rata Siswa Kelas {kelas}: {rata_rata}')