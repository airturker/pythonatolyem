# dosyaya yazma, dosya varsa siler yeni baştan açar. dosya yoksa oluşturur.

ths = open("tahsilat_dosyası.txt", "w",encoding="utf-8")
ths.write("Halil Pazarlama: 120.000 TL")
ths.close()