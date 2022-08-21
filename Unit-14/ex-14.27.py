import tkinter as tk
from tkinter import ttk

mainfrm = tk.Tk()

mbtFile = ttk.Menubutton(mainfrm, text="File", width=10)
mbtFile.grid(column=0,row=0)
mbtHelp = ttk.Menubutton(mainfrm, text="Help", width=10)
mbtHelp.grid(column=3,row=0)

mnFile = tk.Menu(mbtFile, tearoff=0)
mbtFile["menu"] = mnFile
mnFile.add_checkbutton(label="New")
mnFile.add_checkbutton(label="Open")
mnFile.add_checkbutton(label="Save")
mnFile.add_checkbutton(label="Exit")

mnHelp = tk.Menu(mbtHelp, tearoff=0)
mbtHelp["menu"] = mnHelp
mnHelp.add_checkbutton(label="Help Topics")
mnHelp.add_checkbutton(label="About")

mainfrm.mainloop()