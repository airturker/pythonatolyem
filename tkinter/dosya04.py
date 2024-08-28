import tkinter as tk

window = tk.Tk()

yazi_kutu = tk.Text(
    fg="blue",
    bg="yellow",
    width=50,
    height=20
)
yazi_kutu.insert("1.0","türker")
yazi_kutu.insert("2.0","\nözakıncı")
yazi_kutu.insert("3.0","\nantalya")

yazi_kutu.pack()

window.mainloop()