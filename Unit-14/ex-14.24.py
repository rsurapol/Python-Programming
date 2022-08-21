from tkinter import *
from tkinter import ttk

mainfrm = Tk()
lblFrame = ttk.LabelFrame(mainfrm, text="Login")
lblFrame.pack(padx=10, pady=10)

lblName = ttk.Label(lblFrame, text="User name:").grid(column=0,row=0)
lblPass = ttk.Label(lblFrame, text="Password:").grid(column=0,row=1)

entName = ttk.Entry(lblFrame,).grid(column=1,row=0)
entPass = ttk.Entry(lblFrame,).grid(column=1,row=1)

btnEnter = ttk.Button(lblFrame, text="Enter").grid(column=0,row=3, pady=5)
btnCancel = ttk.Button(lblFrame, text="Cancel").grid(column=1,row=3)

mainfrm.mainloop()