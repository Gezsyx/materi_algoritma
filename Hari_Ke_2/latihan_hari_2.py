nama = str(input("Masukan Nama : "))
jam = int(input('Jumlah Jam Kerja : '))
tarif = int(input("Tarif/Jam : "))
libur = int(input("Libur/bulan : "))

jam_bulan = jam * 20 - libur

gaji = jam_bulan * tarif

print(f"Nama Karyawan : {nama}, Gaji : {gaji}")