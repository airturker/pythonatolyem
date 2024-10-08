# "n" or "N" to align to the top-center part of the cell
# "e" or "E" to align to the right-center side of the cell
# "s" or "S" to align to the bottom-center part of the cell
# "w" or "W" to align to the left-center side of the cell
# "ne" or "NE" to align north-east
# "nw" or "NW" to align north-west
# "se" or "SE" to align south-east
# "sw" or "SW" to align south-west

import tkinter as tk

window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sw")

window.mainloop()