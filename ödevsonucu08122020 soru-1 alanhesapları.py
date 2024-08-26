print ("""
1- karenin alanı
2- dikdörtgenin alanı
3- üçgenin alanı
4- dairenin alanı
""")

def karealan():
    kenar=int(input("lütfen karenin bir kenarını giriniz: "))
    alankare=kenar*kenar
    print("karenin alanı: ", alankare, "cm^2 dir.")
    print("-----------------------------")

def dikdortgenalan():
    kisakenar=int(input("lütfen dikdörtgenin kısakenarı giriniz: "))
    uzunkenar=int(input("lütfen dikdörtgenin uzunkenarı giriniz: "))
    alandikdortgen = kisakenar*uzunkenar
    print("dikdörtgenin alanı: ", alandikdortgen, "cm^2 dir.")
    print("-----------------------------")
    
def ucgenalan():
    yukseklik=int(input("lütfen üçgenin yüksekliğini giriniz: "))
    tabanuzunluk=int(input("lütfen üçgenin taban uzunluğunu giriniz: "))
    alanucgen=(yukseklik*tabanuzunluk)/2
    print("üçgenin alanı: ", alanucgen, "cm^2 dir.")
    print("-----------------------------")

def dairealan():
    yaricap=int(input("lütfen dairenin yarıçapını giriniz: "))
    alandaire=(3.24 * yaricap**2)
    print("dairenin alanı: ", alandaire ,"cm^2 dir.")
    print("-----------------------------")
    


while 1:
    secim = input("Seçiminiz (1/2/3/4): ")
    
    if secim=="1":
        karealan()
    
    elif secim=="2":
        dikdortgenalan()
        
    elif secim=="3":
        ucgenalan()
        
    elif secim=="4":
        dairealan()
    
    else:
        print("lütfen (1/2/3/4) giriniz...")
    
    devam = input("devam etmek istermisiniz: ")
    if devam=="e":
        secim
    else:
        print("teşekkürler...")
        break

