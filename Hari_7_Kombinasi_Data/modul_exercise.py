list_buku = [
    {'Judul': "Dalim 1990", 'Jenis': "Novel"},
    {'Judul': "Laskar Pelangi", 'Jenis': "Novel"},
    {'Judul': "Belajar Python", 'Jenis': "Novel"}
]
judul = "pp"
jenis = "lk"
template = {"Judul": judul, "Jenis": jenis}
list_buku.append(template)
del list_buku[0]
print(list_buku)