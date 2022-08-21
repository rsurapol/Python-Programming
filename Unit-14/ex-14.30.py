from tkinter import *
from tkinter import ttk

mainfrm = Tk()

frmTab1 = ttk.Frame(mainfrm)
frmTab2 = ttk.Frame(mainfrm)
ntb = ttk.Notebook(mainfrm, height=100, width=100)
ntb.add(frmTab1, text="ข้อมูลทั่วไป")
ntb.add(frmTab2, text="ข้อมูลส่วนตัว")

ntb.pack(padx=20, pady=20)

mainfrm.mainloop()