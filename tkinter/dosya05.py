import tkinter as tk

window = tk.Tk()

cerceve_1 = tk.Frame()
cerceve_2 = tk.Frame()

label_a = tk.Label(master=cerceve_1, text="ben çerçeve A dayım")
label_a.pack()

label_b = tk.Label(master=cerceve_2, text="ben çerçeve B deyim")
label_b.pack()

cerceve_1.pack()
cerceve_2.pack()

window.mainloop()