nama = str (input("NAMA KARYAWAN :")).upper()
pekerjaan = str (input("JABATAN (DESAIGN/PROGRAMMER/RESOURCE) :")).upper()
status = str (input("STATUS PERKAWINAN (Y/T) :")).upper()

list_jabatan = {"DESAIGN", "PROGRAMMER", "RESOURCE"} 


if pekerjaan in list_jabatan and pekerjaan == "DESAIGN" or pekerjaan == "RESOURCE":
        gaji = 5000000
        if status == "Y":
              tunjangan_keluarga = gaji * 20/100
        elif status == "T":
              tunjangan_keluarga = 0
        else:
              print("MASUKAN DATA DENGAN BENAR!!!")
               
elif pekerjaan in list_jabatan and pekerjaan == "PROGRAMMER":
        gaji = 10000000
        if status == "Y":
              tunjangan_keluarga = gaji * 20/100
        elif status == "T":
              tunjangan_keluarga = 0        
        else:
              print("MASUKAN DATA DENGAN BENAR!!!")

else:
    print("MASUKAN DATA DENGAN BENAR!!!")

gaji_kotor = gaji + tunjangan_keluarga
pajak = gaji * 10/100
pendapatan = gaji_kotor - pajak

print(" ")
print("=== RINCIAN GAJI KARYAWAN ===")
print("NAMA KARYAWAN :", nama)
print("JABATAN :", pekerjaan)
print(f'GAJI POKOK : Rp.{gaji:,.2f}')
if tunjangan_keluarga > 0:
    print(f'TUNJANGAN KELUARGA : Rp.{tunjangan_keluarga:,.2f}')
print(f'GAJI KOTOR : Rp.{gaji_kotor:,.2f}')
print(f'PAJAK : Rp.{pajak:,.2f}')
print(f'TOTAL PENDAPATAN : Rp.{pendapatan:,.2f}')