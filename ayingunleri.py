print("pt", "sa", "çr", "pr", "cu", "ct", "pz")

# Bir ayın gün sayısını belirliyoruz (Örneğin: 30 gün)
gun_sayisi = 30

# İlk haftadan başlamak üzere günleri 7 sütun halinde yazdırıyoruz
for gun in range(1, gun_sayisi + 1):
    # Günü yazdır ve ardından boşluk ekle
    print(f"{gun:2}", end=" ")
    
    # Eğer gün 7'nin katıysa, yani bir hafta tamamlandıysa, alt satıra geç
    if gun % 7 == 0:
        print()

# Eğer son satır dolu değilse, aşağıda kalan günleri yazdırabilmek için alt satıra geçiyoruz
if gun_sayisi % 7 != 0:
    print()
