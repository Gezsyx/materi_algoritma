antrian = []

def tampilan():
    print("="*100)
    print(f"Antrian Sekarang : {front()} ")
    print(f"Antrian Selanjutnya : {second()} ")
    print(f"Jumlah Antrian :{jumlah()}")

    print('''Pilihan
          1. Tambah Antrian
          2. Lanjut ke Antrian Selanjutnya
          3. Lihat Antrian
          4. Keluar
''')

def isempty(): 
    return len(antrian) == 0

def enqueue(value):
    antrian.append(value)
    print(f'"{value}" ditambahkan ke dalam antrian')

def dequeue():
    if isempty():
        print("Tidak Ada Antrian Selanjutnya!")
    else:
        hapus = antrian.pop(0)
        print(f"{hapus} Telah Selesai")

def jumlah():
    if isempty():
        return "Antrian Kosong"
    else:
        return len(antrian)

def front():
    if isempty():
        return "Antrian Kosong"
    else:
        return antrian[0]

def second():
    if isempty() or len(antrian) == 1:
        return "Antrian Kosong"
    else:
        return antrian[1]

def daftar():
    if isempty():
        print("Antrian Kosong")
    else:
        for i, data in enumerate(antrian,1):
            print(f'Antrian Ke-{i} {data}')


