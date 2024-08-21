# Kontrol edilecek kelimeyi belirliyoruz
kelime = "python"

# Kullanıcıdan kelimeyi doğru girmesini iste
while True:
    tahmin = input("Kelimeyi giriniz: ")
    
    # Kullanıcının girdiği kelimenin uzunluğu, orijinal kelime uzunluğuna eşit olmalı
    if len(tahmin) != len(kelime):
        print(f"Lütfen {len(kelime)} karakter uzunluğunda bir kelime giriniz.")
        continue
    
    # Tahmin edilen kelimeyi kontrol et ve sonuçları göster
    sonuc = ""
    for orijinal, girilen in zip(kelime, tahmin):
        if orijinal == girilen:
            sonuc += "*"
        else:
            sonuc += "?"
    
    print(sonuc)
    
    # Eğer tüm karakterler doğruysa, döngüden çık
    if sonuc == "*" * len(kelime):
        print("Tebrikler, doğru kelimeyi buldunuz!")
        break
