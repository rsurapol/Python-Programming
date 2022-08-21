from tkinter import *
from tkinter import ttk

mainfrm = Tk()

ttk.Entry(mainfrm).grid(column=0, row=0, padx=20, pady=2)
ttk.Entry(mainfrm).grid(column=0, row=1, padx=20, pady=2)
ttk.Entry(mainfrm).grid(column=0, row=2, padx=20, pady=2)

mainfrm.mainloop()