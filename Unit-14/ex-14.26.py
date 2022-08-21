import tkinter as tk

mainframe = tk.Tk()
menubar = tk.Menu(mainframe)

file = tk.Menu(menubar, tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_separator()
file.add_command(label="Exit")
menubar.add_cascade(label="File", menu=file)

_help = tk.Menu(menubar, tearoff=0)
_help.add_command(label="Help Topics")
_help.add_command(label="Shortcut key")
_help.add_separator()
_help.add_command(label="About")
menubar.add_cascade(label="Help", menu=_help)

mainframe.config(menu=menubar)
mainframe.mainloop()