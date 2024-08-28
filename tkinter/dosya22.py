import tkinter as tk

window = tk.Tk()

def tikla():
    etiket["text"] = giris.get()

giris = tk.Entry()
giris.pack()

dugme = tk.Button(text="tıkla!", command = tikla)
dugme.pack()

etiket = tk.Label(text="alinti")
etiket.pack()

window.mainloop()