from tkinter import *
from tkinter import ttk

mainfrm = Tk()

chkM = ttk.Checkbutton(mainfrm, text="ชาย").grid(column=0, row=0, padx=20, pady=20)
chkF = ttk.Checkbutton(mainfrm, text="หญิง").grid(column=1, row=0, padx=20, pady=20)

mainfrm.mainloop()