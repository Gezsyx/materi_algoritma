class Mobil:
    # Membuat atribut
    def __init__(self,merk,warna):
        self.merk = merk
        self.warna = warna

    # Membuat metode
    def setMerk(self,item):
        self.merk = item
    def setwarna(self,item2):
        self.warna = item2


    def information(self):
        return f"Merk Mobil : {self.merk} | Warna Mobil : {self.warna}"
    
mobil1 = Mobil("Pajero","Putih")
mobil1.setMerk("Chevrolet")
mobil1.setwarna("kuning")

mobil2 = Mobil("Kijang","Hitam")
print(mobil1.information())
print(mobil2.information())


# class Matematika:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b

#     def LuasPersegiPanjang(self):
#         return self.a*self.b
    
# objek1 = Matematika(10,60)
# print(objek1.LuasPersegiPanjang())