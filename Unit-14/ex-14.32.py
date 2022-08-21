from tkinter import *
from tkinter import ttk

mainfrm = Tk()

pgb1 = ttk.Progressbar(mainfrm, mode="determinate", length=200)
pgb1.pack(padx =10, pady=10)
pgb2 = ttk.Progressbar(mainfrm, mode="indeterminate", length=200)
pgb2.pack(padx =10, pady=10)
pgb1.start()
pgb2.start(100)

mainfrm.mainloop()