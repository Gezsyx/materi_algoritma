from queue import LifoQueue

riwayat = []
sampah = []

riwayat.append("1")
riwayat.append("2")
riwayat.append("3")

hapus = riwayat[-1]
sampah.append(hapus)
riwayat.pop()

hapus = sampah[-1]
riwayat.append(hapus)
riwayat.pop()

print(riwayat)
print(sampah)