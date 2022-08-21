from tkinter import *
from tkinter import ttk

mainfrm = Tk()

ttk.Label(mainfrm, text="Lable 1").grid(column=0, row=0, padx=50, pady=2)
ttk.Label(mainfrm, text="Lable 2").grid(column=0, row=1, padx=50, pady=2)
ttk.Label(mainfrm, text="Lable 3").grid(column=0, row=2, padx=50, pady=2)

mainfrm.mainloop()