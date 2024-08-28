# 1’den 100’e kadar olan asal sayıları bulup dosyaya kaydeden program.

asal_sayi=[]    # asal sayıların kaydedileceği liste tanımlandı
for sayi in range(2,100): # asal sayıların tek tek sınanması için döngü kuruldu
   if sayi > 1:
       for i in range(2,sayi):
           if (sayi % i) == 0:
               break
       else:
           asal_sayi.append(sayi)

veri=" "  # yukarıdaki listedeki sayıları atmak için değişken tanımlandı
for i in asal_sayi:   #yukarıda bulunan asal sayılar döng ile tek tek alındı
  veri+=str(i) # dosyaya string olarak yazılabildikleri için dönüştürüldü.
  veri+=" "

dosya=open ("asalsayı.txt","w") # dosya yazma işlemi için açıldı
dosya.write(veri) # dosyaya veri değişkenindekiler yazıldı.
dosya.close() 