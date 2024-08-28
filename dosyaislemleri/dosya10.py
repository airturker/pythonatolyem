# satır değiştirme

with open("kayıtlar.txt", "r",encoding="utf-8") as k:
    veri = k.readlines()
    del veri[1]
    print(veri)

with open("kayıtlar.txt", "w",encoding="utf-8") as k:
    veri.insert(1, "Sedat Köz\n")
    print(veri)
    k.seek(0)
    k.writelines(veri)  #yenilenen listeyi satır satır yazdırır.