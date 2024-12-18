import pandas as pd

# arry = {
    # 'Senin' : [10,5,3],
    # 'Selasa' : [6,7,8],
    # 'Rabu' : [20,15,10],
    # 'Kamis' : [5,3,2],
    # 'Jumat' : [15,18,12],
    # 'Sabtu' : [10,5,6],
# }

df = pd.DataFrame([
    [10,5,3],
    [6,7,8],
    [20,15,10],
    [5,3,2],
    [15,18,12],
    [10,5,6],
], index=['Senin', 'Selasa', 'Rabu','Kamis','Jumat','Sabtu'], 
columns=['Barang A', "Barang B", "Barang C"])

index_penjualan_tertinggi_hari = df.idxmax(axis=1)
index_penjualan_tertinggi = df.idxmax(axis=0)
df['Total']=df.sum(axis=1)


print(df)
print(index_penjualan_tertinggi_hari)
print(index_penjualan_tertinggi)

df.to_csv('DataPenjualan.csv')