from tkinter import *
from tkinter import ttk

mainfrm = Tk()

frmTop = ttk.Frame(mainfrm, relief="groove", borderwidth=5)
frmTop.pack()

frmBottom = ttk.Frame(mainfrm, relief="groove", borderwidth=5)
frmBottom.pack()

ttk.Button(frmTop, text="Entry1").pack()

ttk.Button(frmBottom, text="Entry2").pack(side="right")
ttk.Button(frmBottom, text="Entry3").pack(side="left")

mainfrm.mainloop()