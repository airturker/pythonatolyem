# seek() dosya içinde istediğimiz karaktere bizi götürür.
# tell() dosya içinde hangi karakterde olduğumuzu gösterir.

with open(".\\dosyaislemleri\\deneme.txt", encoding="utf-8") as dosya:
        dosya.seek(10)
        print(dosya.read())