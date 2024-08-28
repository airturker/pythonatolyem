# 'r+' bir dosyayı hem okuma hem de yazma kipinde açmamıza yardımcı olur. bu örnek dosyanın başına ekleme yapmak için hazırlanmıştır.

with open("fihrist.txt", "r+",encoding="utf-8") as f:
    veri = f.read() # dosyayı bir değişkene atıyor.
    f.seek(0) #Dosyayı başa sarıyoruz
    f.write("Sedat Köz\t: 0322 234 45 45\n"+veri) # istenileni ekleyip sonuna da dosyayı ekliyor.