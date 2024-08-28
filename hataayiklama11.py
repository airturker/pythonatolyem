# hata yokken hata mesajı görüntülemek
tr_karakter = "şçğüöıİ"

parola = input("Parolanız: ")

for i in parola:
    if i in tr_karakter:
        raise Exception("Parolada Türkçe karakter kullanılamaz!")
    else:
        pass

print("Parola kabul edildi!")