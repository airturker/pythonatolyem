# dosyaya yazma, dosya varsa siler yeni baştan açar. dosya yoksa oluşturur.

ths = open(".\\dosyaislemleri\\tahsilat_dosyası.txt", "w",encoding="utf-8")
ths.write("nehir Pazarlama: 300.000 TL")
ths.close()