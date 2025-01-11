import random
angka_rahasia = random.randint(1, 50)
percobaan = int(0)
print("Selamat Datang di GACORHARBER515!".upper())
depo = int(input("Masukan Jumlah Untuk Depo (Minimal 5.000): ".upper()))
hadiah = int (random.randint(1000, 50000))

if depo >= 5000:
    max = depo/1000
    bonus = depo*60/100
    hadiah += bonus
    print(f"Anda Memiliki {max} Kesempatan Menebak".upper())
    while True:
        print("Tebak angka antara 1 sampai 50.")
        tebakan = int(input("Masukkan tebakan Anda: "))
        percobaan += 1
        cashback = max - percobaan

        if tebakan == angka_rahasia:
            print("="*100)
            print(f"GACOR KANG! Anda Mendapatkan Rp.{hadiah:,.2f} di {percobaan} Kali Percobaan.".upper())
            print(f"Anda mendapatkan cashback Rp.{cashback*1000:,.2f}")
            break
        elif percobaan == max:
            print("="*100)
            print(f"Angka Yang Benar Adalah {angka_rahasia}".upper())
            print(f"Kesempatan Anda Sudah Habis, Coba Lagi Lain Kali!".upper())
            break

        else:
            print("="*100)
            print("Anda Kurang Beruntung!")
            print(f"Kesempatan menebak Tinggal {max - percobaan} Kali Percobaan".upper())
    
else:
    print("="*100)
    print(f"MINGGIR LU MISKIN!")
    
        


# while True:
#     tebakan = int(input("Masukkan tebakan Anda: "))
#     percobaan += 1

#     if tebakan == angka_rahasia:
#         print(f"GACOR KANG! Anda Mendapatkan Rp.100.000.000,00 di {percobaan} Kali Percobaan.")
#         break
#     elif percobaan == max:
#         print(f"Angka Yang Benar Adalah {angka_rahasia}")
#         print(f"Kesempatan Anda Sudah Habis, Coba Lagi Lain Kali!")
#         break

#     else:
#         print("Anda Kurang Beruntung!")
#         print(f"Tinggal {10 - percobaan} Kali Percobaan")