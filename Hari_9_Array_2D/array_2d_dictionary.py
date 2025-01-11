arry_2d = {
    'Senin' : [1,2,3],
    'Selasa' : [4,5,6],
    'Rabu' : [7,8,9],
}

print(arry_2d['Senin'][2])

for hari,value in arry_2d.items():
    print(hari,value[0])