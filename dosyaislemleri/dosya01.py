# varolan dosyayı okur (r)

dosya = open (".\\dosyaislemleri\\deneme.txt","r", encoding="utf-8")

belge=dosya.read()

print (belge)

dosya.close()