import array
import sys

arr_1d = array.array('i',[80,100,75,70])
arr_1d_list = [80,100,75,70]

# print(sys.getsizeof(f'Penyimpanan md array :{arr_1d}'))
# print(sys.getsizeof(f'Penyimpanan list array :{arr_1d_list}'))

# cara 2
print(f'MD Array : {sys.getsizeof(arr_1d)}')
print(f'Array List : {sys.getsizeof(arr_1d_list)}')