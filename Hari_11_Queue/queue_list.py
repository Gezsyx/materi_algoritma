# inisialisasi queue (tempat simpan data)

queue = []


# fungsi
def enqueue(value):
    queue.append(value)
    print(f'"{value}" ditambahkan ke dalam antrian')

def dequeue():
    if isempty():
        print('Queue kosong')
    else:
        remove_item = queue.pop(0)
        print(f"{remove_item} dikeluarkan dari queue")

def front():
    # print(f'Antrian Pertama{queue[0]}')
    if isempty():
        return "Kosong"
    else :
        return queue[0]


def isempty():
    return len(queue) == 0


# pemanggilan fungsi
print(f'Antrian kosong : {isempty()}')
print(f'data pertama : {front()}')
antrian = input(str("Masukan Nama :"))
enqueue(antrian)

print(f'Antrian kosong : {isempty()}')
print(f'data pertama : {front()}')

# menghapus data pertama
dequeue()

print(f"Daftar Antrian{queue}")