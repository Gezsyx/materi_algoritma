import random

# Define motorcycle types and their rarities
motorcycles = {
    "mythic": ["h2", "panigale", "s1000rr"],
    "legend": ["zx10r", "Hayabusa", "yzf r7"],
    "epic": ["zx4r", "cbr 400rr", "gsx r400rr"],
    "rare": ["zx25r", "cbr 250rr", "r25"]
}

probabilities = {
    "mythic": 1,
    "legend": 4,
    "epic": 15,
    "rare": 80
}

def draw_motorcycle(warranty):
    if warranty == 160:
        return random.choice(motorcycles["mythic"])

    random_value = random.randint(1, 100)
    for rarity, prob in probabilities.items():
        random_value -= prob
        if random_value <= 0:
            return random.choice(motorcycles[rarity])

def main():
    warranty = 0
    while True:
        warranty += 1
        motorcycle = draw_motorcycle(warranty)
        print(f"You got a {motorcycle} motorcycle!")
        if motorcycle in motorcycles["mythic"]:
            warranty = 0  # Reset warranty after getting a mythic motorcycle
        
        # You can add more logic here, like tracking user's motorcycle inventory, etc.

if __name__ == "__main__":
    main()








































































# import random

# # Daftar item dengan tipe dan probabilitas
# items = {
#     "mythic": ["item1", "item2", "item3"],
#     "legend": ["item7", "item6"],
#     "epic": ["gjh", "hjj"],
#     "rare": ["hjkj", "kjhkj"]
# }
# probabilities = {
#     "mythic": 1,
#     "legend": 4,
#     "epic": 15,
#     "rare": 80
# }

# def gacha(jumlah_gacha):
#     results = []
#     for _ in range(jumlah_gacha):
#         if jumlah_gacha == 50:
#             results.append("item1")  # Hadiah mythic otomatis di gacha ke-50
#         else:
#             random_value = random.randint(1, 100)
#             for tipe, prob in probabilities.items():
#                 random_value -= prob
#                 if random_value <= 0:
#                     results.append(random.choice(items[tipe]))
#                     break
#     return results

# while True:
#     mata_uang = int(input("Masukkan jumlah mata uang: "))
#     if mata_uang % 10 == 0 and mata_uang > 10:
#         pilihan = input("Gacha 1 kali (1) atau 10 kali sekaligus (10)? ")
#         if pilihan == "1":
#             hasil = gacha(1)
#         elif pilihan == "10":
#             hasil = gacha(10)
#         else:
#             print("Pilihan tidak valid.")
#             continue
#     else:
#         hasil = gacha(mata_uang)

#     print("Hasil gacha:")
#     for item in hasil:
#         print(item)