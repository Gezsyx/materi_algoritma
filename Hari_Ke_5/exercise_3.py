import random
mythic = {'BMW S1000RR', 'KAWASAKI NINJA H2', 'DUCATI PANIGALE V4', "SUZUKI GSX-R1000RR", 'YAMAHA YZF-R1', 'HONDA CBR 1000RR', 'APRILIA RSV 100 RR'}
legend = {"HONDA CBR 600RR", "YAMAHA YZF-R7", "YAMAHA YZF-R6", "KAWASASKI NINJA ZX6R", "KAWASAKI NINJA ZX10R", "KAWASAKI NINJA ZX14R", "SUZUKI HAYABUSA", "KTM RC-8C"}
epic = {"HONDA CBR 400RR", "KAWASAKI NINJA ZX4R", "SUZUKI GSX-R400RR", "KTM RC-390"}
rare = {"HONDA CBR 250RR", "YAMAHA YZF-R25", "KAWASAKI NINJA ZX25R", "KAWASAKI NINJA 250RR", 'SUZUKI GSX-250RR'}
items = [random.randint(mythic), random.randint(legend), random.randint(epic), random.randint(rare)]





# # Daftar item dengan tingkat kelangkaan (semakin kecil nilai, semakin langka)
# items = [
#     {"name": "Item Biasa", "rarity": 100},
#     {"name": "Item Langka", "rarity": 50},
#     {"name": "Item Sangat Langka", "rarity": 10},
#     {"name": "Item Legendaris", "rarity": 1}
# ]

# def gacha(jumlah_gacha):
#     results = []
#     for _ in range(jumlah_gacha):
#         total_rarity = sum(item["rarity"] for item in items)
#         random_value = random.randint(1, total_rarity)
#         for item in items:
#             random_value -= item["rarity"]
#             if random_value <= 0:
#                 results.append(item["name"])
#                 break
#     return results

# # Contoh penggunaan
# hasil_gacha = gacha(10)
# print(hasil_gacha)