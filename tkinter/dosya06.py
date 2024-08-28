import tkinter as tk

# tk.FLAT     : Has no border effect (the default value).
# tk.SUNKEN   : Creates a sunken effect.
# tk.RAISED   : Creates a raised effect.
# tk.GROOVE   : Creates a grooved border effect.
# tk.RIDGE    : Creates a ridged effect.

window = tk.Tk()

frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=10, bg="red")
frame.pack(side=tk.LEFT)

label = tk.Label(master=frame, text="relief örneği", bg="yellow")
label.pack()

window.mainloop()