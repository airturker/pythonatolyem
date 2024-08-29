# ilk satırı siler yerine bunu ekler.

with open(".\\dosyaislemleri\\fihrist.txt", "r+",encoding="utf-8") as f:
    f.seek(0)
    f.write("Sedat Köz\t: 0322 234 45 45\n")