from tkinter import *
from tkinter import ttk

mainfrm = Tk()
ttk.Frame(height=80, width=200).pack()

ttk.Style().configure("enter.TButton", font=("Times", "10", "bold"))
ttk.Style().configure("cancel.TButton", font=("Times", "10","italic") )

btnEnter = ttk.Button(mainfrm, text="Enter",  style="enter.TButton").place(x=10, y=30)
btnCancel = ttk.Button(mainfrm, text="Cencle",  style="cancel.TButton").place(x=100, y=30)

mainfrm.mainloop()