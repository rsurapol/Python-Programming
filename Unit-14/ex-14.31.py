from tkinter import *
from tkinter import ttk

mainfrm = Tk()
ttk.Style().configure("s1.TPanedwindow", background="red")
ttk.Style().configure("s2.TPanedwindow", background="green")

pnwLeft = ttk.PanedWindow(mainfrm, height=150, width=100, style="s1.TPanedwindow")
pnwLeft.pack(side="left")
pnwright = ttk.PanedWindow(mainfrm, height=150, width=100, style="s2.TPanedwindow")
pnwright.pack(side="right")

mainfrm.mainloop()