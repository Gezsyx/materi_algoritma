import numpy as np

# array_1d = np.array([1,2,3,4,5])
# print("Array 1 Dimensi:", array_1d)

# # rentang angka
# print("="*100)
# array_range = np.arange(0,10,2)
# print("Array dengan arange:", array_range)

# # operasi aritmatika
# print("="*100)
# arr = np.array([1,2,3,4,5])

# print("penjumlahan:", arr + 2)
# print("perkalian:", arr * 3)
# print("pengurangan:", arr - 1)
# print("pembagian:", arr / 2)

# Statistik numpy
print("="*100)
arr = np.array([1,2,3,4,5])

print(f"Jumlah Data: {len(arr)}")
print("Rata-rata:", np.mean(arr))
print("Jumlah total:", np.sum(arr))
print("Nilai Max:", np.max(arr))
print("Nilai Min:", np.min(arr))
print(f"Jumlah nilai di atas rata rata:{np.sum(arr >= np.mean(arr))}")


# slicing index

arr = np.array([90,81,77,60,70])
print(arr[1:4])
