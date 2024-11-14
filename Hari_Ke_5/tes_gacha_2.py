import random

def gacha(primogems):
  # Tabel peluang (contoh sederhana)
  item_probabilities = {
    "Bintang 5": 0.6,  # 0.6% peluang mendapatkan bintang 5
    "Bintang 4": 5.1,  # 5.1% peluang mendapatkan bintang 4
    "Item Lainnya": 94.3  # Sisanya adalah item lainnya
  }

  # Pity system (contoh sederhana)
  pity = 0
  pity_for_5star = 90

  while primogems > 0:
    primogems -= 1
    pity += 1

    # Generate angka random antara 0 dan 100
    random_number = random.uniform(0, 100)

    # Cek peluang berdasarkan angka random
    for item, probability in item_probabilities.items():
      if random_number <= probability:
        if item == "Bintang 5":
          print("Selamat! Anda mendapatkan item Bintang 5!")
          pity = 0
        elif item == "Bintang 4":
          print("Anda mendapatkan item Bintang 4!")
        else:
          print("Anda mendapatkan item lainnya.")
        break

    # Jika sudah mencapai pity untuk bintang 5, maka pasti mendapatkan bintang 5
    if pity >= pity_for_5star:
      print("Pity reached! Anda mendapatkan item Bintang 5!")
      pity = 0

  print("Primogem habis.")

# Input jumlah Primogem
primogems = int(input("Masukkan jumlah Primogem: "))

# Mulai gacha
gacha(primogems)