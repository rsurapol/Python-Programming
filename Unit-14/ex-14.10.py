import tkinter as tk

mainfrm = tk.Tk()
tk.Frame(height=120, width=290).pack()

tk.Button(mainfrm, text="Enter", height=3, width=10, relief="flat").place(x=10, y=30)
tk.Button(mainfrm, text="Cencle", height=3, width=10, relief="sunken").place(x=90, y=30)
tk.Button(mainfrm, text="Cencle", height=3, width=10, relief="ridge").place(x=180, y=30)

mainfrm.mainloop()