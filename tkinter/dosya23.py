import tkinter as tk

def topla():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    sonuc['text']=str(s1+s2)

pencere=tk.Tk()

sayi1=tk.Entry()
sayi1.pack()

sayi2=tk.Entry()
sayi2.pack()

dugme=tk.Button(text="topla", command=topla)
dugme.pack()

sonuc=tk.Label(text="SONUÇ :")
sonuc.pack()

pencere.mainloop()