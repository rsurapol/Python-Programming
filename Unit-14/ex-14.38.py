import tkinter as tk

mainframe = tk.Tk()

spb = tk.Spinbox(mainframe, from_=0, to=20, format="%10.2f")
spb.grid(column=0, row=0, padx=30, pady=30)

mainframe.mainloop()