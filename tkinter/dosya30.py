import tkinter as tk

OptionList = [
"Ford",
"Reno",
"Fiat",
"Mercedes"
] 

app = tk.Tk()
app.geometry('300x300')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack(side="top")


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

def callback(*args):
    labelTest.configure(text="seçiminiz :  {}".format(variable.get()))

variable.trace("w", callback)

app.mainloop()