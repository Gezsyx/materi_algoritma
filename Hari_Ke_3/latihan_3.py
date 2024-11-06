nama = str(input("Masukan Nama : "))
umur = int(input('Umur : '))
pekerjaan = str(input("Pekerjaan Orang Tua : "))
gaji = float(input("Gaji Orang Tua : "))
ipk = float(input("IPK : "))

list_pekerjaan = ["PNS", "DOKTER", "TNI"]


if (umur <25 and ipk >= 2.7 and gaji <= 1000000 and pekerjaan.upper() not in list_pekerjaan):
    hasil = 'Lolos Beasiswa'  
else:
    hasil = 'Tidak Lolos Beasiswa'
    

print('='*5)
print ("NAMA :", nama.upper())
print ("UMUR :", umur)
print ("PEKERJAAN ORAMG TUA :", pekerjaan.upper())
print ("GAJI ORANG TUA :", gaji)
print ("IPK :", ipk)
print (hasil)    

