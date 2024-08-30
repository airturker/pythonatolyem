import tkinter as tk

window = tk.Tk()

window.geometry("400x300")

window.title("python öğreniyorum")

selamla = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="red",
    width=10,
    height=30
    )

selamla.pack()

window.mainloop()