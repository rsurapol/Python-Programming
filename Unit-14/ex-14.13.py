from tkinter import *
from tkinter import ttk

mainfrm = Tk()
ttk.Frame(height=80, width=200).pack()

ttk.Button(mainfrm, text="Enter", cursor="mouse").place(x=10, y=30)
ttk.Button(mainfrm, text="Cencle", cursor="x_cursor").place(x=100, y=30)

mainfrm.mainloop()