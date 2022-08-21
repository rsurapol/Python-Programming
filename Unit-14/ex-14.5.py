from tkinter import *
from tkinter import ttk

mainfrm = Tk()
ttk.Frame(mainfrm, height=180, width=250).pack()

ttk.Button(mainfrm, text="Enter").place(height=30, width=80)
ttk.Button(mainfrm, text="Cancel").place(height=30, width=80, x=85, y=0)
ttk.Button(mainfrm, text="Clear").place(height=30, width=80, x=170, y=0)

ttk.Button(mainfrm, text="Enter").place(height=30, width=80, x=85, y=40)
ttk.Button(mainfrm, text="Cancel").place(height=30, width=80, x=85, y=70)
ttk.Button(mainfrm, text="Clear").place(height=30, width=80, x=85, y=100)

ttk.Button(mainfrm, text="Enter").place(height=30, width=80, x=0, y=140)
ttk.Button(mainfrm, text="Cancel").place(height=30, width=80, x=85, y=140)
ttk.Button(mainfrm, text="Cancel").place(height=30, width=80, x=170, y=140)

mainfrm.mainloop()