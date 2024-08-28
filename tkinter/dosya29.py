from tkinter import *

master = Tk()
master.geometry("300x300")
variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

mainloop()