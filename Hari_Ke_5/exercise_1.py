kelas = str(input('Masukan Kelas: ')).upper()
jumlah = int(input('Masukan Jumlah Mahasiswa:'))
siswa_ke = 1
total = 0

for i in range (jumlah):
    nilai = int(input(f'Masukan Nilai Mahasiswa Ke {siswa_ke} : '))
    total += nilai
    siswa_ke += 1
    rata_rata = total / jumlah

print("="*30)

print(f'Kelas : {kelas}')
print(f'Jumlah Mahasiswa : {jumlah}')
print(f'Nilai Rata-Rata Siswa Kelas {kelas}: {rata_rata}')