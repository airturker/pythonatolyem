# Girilen sayının asal olup olmadığını dosyadan karşılaştıran program

with open("asalsayı.txt","r") as dosya :  # asalsayıların kayıtlı olduğu belge açılır
  veri=dosya.read() # dosya okunur
  asal_sayılar=veri.split(" ")  # okunanlar bir listeye atılır. her boşlukta bir içerik bölünerek atılır.

kontrol_sayısı=input("asal olup olmadığını kontrol etmek istediğiniz sayıyı giriniz: ")
if kontrol_sayısı in asal_sayılar : 
  print("asal sayı")
else:
  print("asal sayı değil")

dosya.close()