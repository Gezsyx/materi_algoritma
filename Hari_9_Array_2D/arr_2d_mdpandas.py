import pandas as pd

df = pd.DataFrame([
    [1,2,3],
    [4,5,6],
    [7,8,9],
], 
index=['Senin', 'Selasa', 'Rabu'], 
columns=['Barang A', "Barang B", "Barang C"])

df['Barang D'] = [10,11,12]

df['Total']=df.sum(axis=1)
# df.loc['Tortal']=df.sum(axis=0)

print(df)

# index_data_tertinggi_perbaris = df.idxmax(axis=0)
# print(index_data_tertinggi_perbaris)

# df.to_csv('Data_Penjualan.csv', sep=';')