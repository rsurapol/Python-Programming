from tkinter import *
from tkinter import ttk

mainfrm = Tk()
ttk.Frame(mainfrm, height=80, width=280).pack()

btnEnter = ttk.Button(mainfrm, text="Enter").place(x=10, y=30)
btnCancel = ttk.Button(mainfrm, text="Cencle").place(x=100, y=30)
btnClear = ttk.Button(mainfrm, text="Clear").place(x=190, y=30)

mainfrm.mainloop()