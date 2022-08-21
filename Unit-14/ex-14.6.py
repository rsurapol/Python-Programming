from tkinter import *
from tkinter import ttk

mainfrm = Tk()

btnEnter = ttk.Button(mainfrm, text="Enter").grid(column=0,row=0, padx=10, pady=10)
btnCancel = ttk.Button(mainfrm, text="Cencle").grid(column=1,row=0, padx=10, pady=10)
btnClear = ttk.Button(mainfrm, text="Clear").grid(column=2,row=0, padx=10, pady=10)

mainfrm.mainloop()