list_buku = [
    {'Judul': "Dalim 1990", 'Jenis': "Novel"},
    {'Judul': "Laskar Pelangi", 'Jenis': "Novel"},
    {'Judul': "Belajar Python", 'Jenis': "Novel"}
]


while True:
    print("="*100)
    print("SELAMAT DATANG DI SISTEM PERPUSTAKAAN")
    print("1. Tambah Buku")
    print("2. Hapus Buku")
    print("3. Lihat Buku")
    print("4. Keluar")
    print("="*100)

    pilih = int(input("Masukan Pilihan : "))
    print("="*100)
    if pilih == 1:
        judul = str(input("Masukan Judul Buku : "))
        jenis = str(input("Masukan Jenis Buku : "))
        template = {"Judul": judul, "Jenis": jenis}
        list_buku.append(template)
        print("="*100)

    elif pilih == 2:
        print("DAFTAR BUKU!")
        x = 1
        for list in list_buku:
            print(x, list['Judul'], list['Jenis'])
            x += 1
        hapus = int(input("Hapus Buku Ke : "))
        del list_buku[hapus-1]

    elif pilih == 3:
        print("DAFTAR BUKU!")
        x = 1
        for list in list_buku:
            print(x, list['Judul'], list['Jenis'])
            x += 1

    elif pilih == 4:
        keluar= str(input(("Yakin Mau Keluar Sekarang?(Y/T) : "))).upper()
        if keluar == "Y":
            print("="*100)
            break
    
    else:
        print("Masukan Pilihan Dengan Benar!")
