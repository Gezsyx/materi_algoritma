import numpy as np

arr_2d = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr_2d[2][2])
print(arr_2d[2,2])

total_perkolom = arr_2d.sum(axis=0)
total_perbaris = arr_2d.sum(axis=1)
angka_tertinggi = arr_2d.max(axis=1)
index_angka_tertinggi = arr_2d.argmax(axis=1)

print(index_angka_tertinggi)
print(angka_tertinggi)
print(total_perkolom)
print(total_perbaris)