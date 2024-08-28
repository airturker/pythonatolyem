# Importing Tkinter module
from tkinter import *
# from tkinter.ttk import *
def sel():
   selection = "seçiminiz : " + v.get()
   label.config(text = selection) 
# Creating master Tkinter window
master = Tk()
master.geometry("200x200")
 
# Tkinter string variable
# able to store any string value
v = StringVar(master, "0")
 
# Dictionary to create multiple buttons
values = {"RadioButton 1" : "acer",
          "RadioButton 2" : "hp",
          "RadioButton 3" : "lenovo",
          "RadioButton 4" : "casper",
          "RadioButton 5" : "apple"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v, command=sel,
                value = value, indicator = 0,
                background = "light blue").pack(fill = X, ipady = 5)
 
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())

label = Label(master)
label.pack()

mainloop()