import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

def tikla():
    messagebox.showinfo("uyarı", "buton tıklandı!")

dugme = tk.Button(text="tıkla!", command=tikla)
dugme.pack()

window.mainloop()