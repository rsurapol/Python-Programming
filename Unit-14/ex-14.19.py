from tkinter import *
from tkinter import ttk, colorchooser

mainfrm = Tk()
cmb = ttk.Combobox(mainfrm, value=("Python","Java", "R", "Scala"), width=20)
cmb.current(0)
cmb.pack(padx=20, pady=20)

mainfrm.mainloop()