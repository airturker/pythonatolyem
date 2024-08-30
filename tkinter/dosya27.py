from tkinter import *

def sel():
   selection = "seçiminiz : " + var.get()
   label.config(text = selection)

root = Tk()
var = StringVar()
var.set(0)
R1 = Radiobutton(root, text="türker", variable=var, value="turker", command=sel)
R1.pack( anchor = E )

R2 = Radiobutton(root, text="kemal", variable=var, value="kemal", command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="ömer", variable=var, value="ömer", command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()