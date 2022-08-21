from tkinter import *
from tkinter import ttk

mainfrm = Tk()
ttk.Frame(mainfrm, height=80, width=200).pack()

ttk.Style().configure("enter.TButton", background="red")
ttk.Style().configure("cancel.TButton", foreground="#FF00CC")

btnEnter = ttk.Button(mainfrm, text="Enter", style="enter.TButton").place(x=10, y=30)
btnCancel = ttk.Button(mainfrm, text="Cencle", style="cancel.TButton").place(x=100, y=30)

mainfrm.mainloop()