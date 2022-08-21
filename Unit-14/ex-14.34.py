from tkinter import *
from tkinter import ttk

mainfrm = Tk()
lblfrm = ttk.LabelFrame(mainfrm, text="Set Scale")
lblfrm.pack()

ttk.Scale(lblfrm, orient=VERTICAL).grid(column=0,row=0, sticky="W")
ttk.Scale(lblfrm, orient=VERTICAL).grid(column=1,row=0, sticky="W")
ttk.Scale(lblfrm, length=150).grid(column=0,row=2, sticky="W")
ttk.Scale(lblfrm, length=150).grid(column=0,row=3, sticky="W")

mainfrm.mainloop()