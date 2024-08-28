# read() bütün dosyayı okur, readline() satır satır okur. eğer read yada readline içine sayı yazılırsa baştan itibaren kaç karakter okuyacağıdır. 

fihrist = open("fihrist.txt",encoding="utf-8")
print(fihrist.readline())
print(fihrist.readline())
print(fihrist.readline())
fihrist.close()
