# varolan dosyayı okur (r)

dosya = open ("deneme.txt","r", encoding="utf-8")

belge=dosya.read()

print (belge)

dosya.close()