# dosya ortalarına ekleme yapmak. satırları kaydırarak.

with open(".\\dosyaislemleri\\fihrist.txt", "r+",encoding="utf-8") as f:
    veri = f.readlines()
    veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n") # 2. indekse eklemeyi yapar.
    f.seek(0)
    f.writelines(veri)  #yenilenen listeyi satır satır yazdırır.

'''
with open("fihrist.txt", "r") as f:
    veri = f.readlines()

with open("fihrist.txt", "w") as f:
    veri.insert(2, "Sedat Köz\t: 0322 234 45 45\n")
    f.writelines(veri)

'''