import tkinter as tk
from tkinter import ttk

mainfrm = tk.Tk()
ttk.Frame(height=110, width=260).pack()

imgSave = tk.PhotoImage(file="D:\PythonFiles\img\save.png")
imgClose = tk.PhotoImage(file="D:\PythonFiles\img\close.png")
imgPrinter = tk.PhotoImage(file="D:\PythonFiles\img\printer.png")

ttk.Button(mainfrm, text="Save", image=imgSave, compound="top").place(x=10, y=10)
ttk.Button(mainfrm, text="Close", image=imgClose, compound="top").place(x=100, y=10)
ttk.Button(mainfrm, text="Print", image=imgPrinter, compound="top").place(x=180, y=10)

mainfrm.mainloop()