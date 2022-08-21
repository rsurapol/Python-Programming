from tkinter import *
from tkinter import ttk

mainfrm = Tk()

ttk.Scrollbar(mainfrm, orient="vertical").pack(side="right", fill="y")
ttk.Scrollbar(mainfrm, orient="horizontal").pack(side="bottom", fill="x")

mainfrm.mainloop()