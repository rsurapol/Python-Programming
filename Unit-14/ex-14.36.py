from tkinter import *
from tkinter import ttk

mainfrm = Tk()

ttk.Label(mainfrm, text="Top").grid(column=0, row=0, padx=100, pady=5)
ttk.Separator(mainfrm,).grid(column=0, row=1, sticky="we", pady=5)
ttk.Label(mainfrm, text="Bottom").grid(column=0, row=2, padx=100, pady=5)

mainfrm.mainloop()