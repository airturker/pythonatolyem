# Rezervasyon kapasite kontrolü uygulaması

dosya=open(".\\dosyaislemleriornek\\rezervasyon_2.txt","r+",encoding="utf-8")
rezervasyonlar=dosya.readlines()

rezervasyon_kapasitesi=5
sıra_no=0 

for rezervasyon_sahibi in rezervasyonlar:
  print(sıra_no+1,"nolu rezervasyon sahibi",rezervasyon_sahibi)
  sıra_no+=1
print("toplam",sıra_no,"adet rezervasyon var")

if rezervasyon_kapasitesi-sıra_no > 0 :
  print(rezervasyon_kapasitesi-sıra_no,"adet daha rezervasyon yapabiliriz")
else:
  print("rezervasyon kapasitemiz dolmuştur.")
dosya.close ()