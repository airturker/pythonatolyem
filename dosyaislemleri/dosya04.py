# readlines(), dosya içeriğini liste olarak verir.

fihrist = open(".\\dosyaislemleri\\fihrist.txt",encoding="utf-8")
print(fihrist.readlines())
fihrist.close()