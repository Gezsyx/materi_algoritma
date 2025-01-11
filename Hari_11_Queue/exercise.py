import modul_exercise as md


while True:
    md.tampilan()
    pilih = int(input("Pilihan (1/2/3/4) : "))

    if pilih == 1:
        nama = str(input("Masukan Nama :"))
        md.enqueue(nama.capitalize())
    if pilih == 2:
        md.dequeue()
    if pilih == 3:
        md.daftar()
    if pilih == 4:
        opsi = str(input("Yakin Ingin Keluar Sekarang? (Y/T) : ")).upper()
        if opsi == "Y":
            break