from tkinter import *
from tkinter import ttk

mainfrm = Tk()

btn1 = ttk.Button(mainfrm, text="Enter").pack(side="left",fill="y")
ttk.Button(mainfrm, text="Cancel").pack(fill="x")
ttk.Button(mainfrm, text="Clear").pack(fill="x", side="right")

mainfrm.mainloop()