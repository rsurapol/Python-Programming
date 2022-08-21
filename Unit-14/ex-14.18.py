from tkinter import *
from tkinter import ttk, colorchooser

mainfrm = Tk()
def color():
    c = colorchooser.askcolor()

btnColor = ttk.Button(mainfrm, text="Show Color", command=color)
btnColor.pack(padx=10, pady=10)

mainfrm.mainloop()