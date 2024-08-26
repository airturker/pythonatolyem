secimler = """
1- elemanları listele(görüntüle)
2- listeye eleman ekleme(ardından listeyi görüntület)
3- listeden eleman silme(ardından listeyi görüntület)
4- listedeki bir elemanı değiştirme
"""

print(secimler)

liste = ["işlemci","ram","monitor","kasa","fare","klavye"]

def listele():
    print(liste)
        
def ekle():
    yeniurun=input("yeni ürün adı giriniz: ")
    liste.append(yeniurun)

def sil():
    urunsil = input("silinecek ürünü giriniz: ")
    liste.remove(urunsil)

def degistir():
    arama=input("listede aranacak kelime: ")
    if arama in liste:
        elemanindexi = liste.index(arama)
        # print(elemanindexi)
        liste[elemanindexi] = input("yeni isim: ")
    else:
        print(arama, "kelimesi yoktur. ")
    
while 1:
    
    secim = input("lütfen seçiminizi giriniz(çıkış için 'q'): ")
    
    if secim=="q":
        print("teşekkürler...")
        break
    
    if secim=="1":
        listele()
    
    if secim=="2":
        ekle()
        listele()
    
    if secim=="3":
        sil()
        listele()
        
    if secim=="4":
        degistir()
        listele()

    