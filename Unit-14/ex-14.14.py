import tkinter as tk
from tkinter import ttk

mainfrm = tk.Tk()
ttk.Frame(height=110, width=260).pack()

imgSave = tk.PhotoImage(file="D:\PythonFiles\img\save.png")
imgClose = tk.PhotoImage(file="D:\PythonFiles\img\close.png")
imgPrinter = tk.PhotoImage(file="D:\PythonFiles\img\printer.png")

ttk.Button(mainfrm, image=imgSave).place(x=10, y=20)
ttk.Button(mainfrm, image=imgClose).place(x=90, y=20)
ttk.Button(mainfrm, image=imgPrinter).place(x=170, y=20)

mainfrm.mainloop()