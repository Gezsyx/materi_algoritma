from queue import LifoQueue

riwayat = []
sampah = []
undo = []

def tampilan ():
    print("="*100)
    if isempty():
        print("Tidak ada riwayat pencarian saat ini")
    else:
        print(f"Riwayat pencarian saat ini : {riwayat}")
    print('''Pilihan :
          1. Tambah Pencarian
          2. Hapus Pencarian Terbaru
          3. Undo
          4. Keluar''')
    
def isempty():
    return len(riwayat) == 0

def push(value):
    riwayat.append(value)

def delete():
    if isempty():
        print("Tidak ada riwayat terbaru")
    else:
        hapus = riwayat[-1]
        sampah.append(hapus)
        riwayat.pop()

def undo_riwayat():
    if isempty():
        print("Tidak ada riwayat yang di hapus")
    else:
        undo = sampah[-1]
        riwayat.append(undo)
        sampah.pop()
        
    