import turtle
def desen_ciz (kenar_uzunluğu=50,ic_kenar=3,tur_sayısı=12):
  kalem=turtle.Turtle()
  for i in range (tur_sayısı):
    for j in range (ic_kenar):
      kalem.forward(kenar_uzunluğu)
      kalem.left(360/ic_kenar)
    kalem.left(30)
  kalem.left(360/tur_sayısı)
  
#desen_ciz()
desen_ciz(60,4,12)
desen_ciz(70,6,12)
turtle.done()