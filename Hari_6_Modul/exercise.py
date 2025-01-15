# import matematika
# from matematika import tambah, kurang, kali

# print("Pilih Operasi Matematika")
# print("1.Tambah")
# print("2.Kurang")
# print("3.Kali")
# print("="*100)

# while True:
#     pilihan = input("Masukkan pilihan (1/2/3): ")

#     print("="*100)

#     if pilihan in ('1', '2', '3'):
#         a = int(input("Masukkan angka pertama: "))
#         b = int(input("Masukkan angka kedua: "))
#         print("="*100)


#         if pilihan == '1':
#             print(f"Hasil {a} + {b} = {tambah(a,b)}")
#         elif pilihan == '2':
#             print(f"Hasil {a} - {b} = {kurang(a,b)}")
#         elif pilihan == '3':
#             print(f"Hasil {a} x {b} = {kali(a,b)}")

#         print("="*100)
#         break
    
# else:.
#     print("Masukkan pilihan dengan benar.")

import matematika as md

while True:
    md.tampilan()
    option = int(input("Masukan Pilihan : "))

    a = int(input("Masukan Angka Pertama : "))
    b = int(input("Masukan Angka Kedua : "))

    if option == 1:
        print(f"Hasil {a} + {b} = {md.tambah(a,b)}")
    elif option == 2:
        print(f"Hasil {a} - {b} = {md.kurang(a,b)}")
    elif option == 3:
        print(f"Hasil {a} x {b} = {md.kali(a,b)}")
    next = str(input("Lanjutkan? (Y/T) : ")).upper()
    if next == "T" :
        print("Anda Menghentikan Program")
        break
    print("="*100)