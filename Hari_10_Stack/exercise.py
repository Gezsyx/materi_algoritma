# from queue import LifoQueue

# riwayat = []
# sampah = []

# riwayat.append("1")
# riwayat.append("2")
# riwayat.append("3")

# hapus = riwayat[-1]
# sampah.append(hapus)
# riwayat.pop()

# hapus = sampah[-1]
# riwayat.append(hapus)
# riwayat.pop()

# print(riwayat)
# print(sampah)

import modul_exercise as md

while True:
    md.tampilan()
    pilih = int(input("Pilihan (1/2/3/4) : "))

    if pilih == 1:
        nama = str(input("Masukan Pencarian :"))
        md.push(nama.capitalize())
    if pilih == 2:
        md.delete()
    if pilih == 3:
        md.undo_riwayat()
    if pilih == 4:
        opsi = str(input("Yakin Ingin Keluar Sekarang? (Y/T) : ")).upper()
        if opsi == "Y":
            break