from tkinter import *
from tkinter import ttk

mainfrm = Tk()
ttk.Frame(mainfrm, height=100, width=150).pack()

ttk.Sizegrip(mainfrm).pack(side="bottom")

mainfrm.mainloop()