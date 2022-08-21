import tkinter as tk

mainfrm = tk.Tk()
tk.Frame(height=150, width=290).pack()

tk.Button(mainfrm, height=30, width=30, bitmap="error").place(x=50, y=60)
tk.Button(mainfrm, height=30, width=30, bitmap="hourglass").place(x=90, y=60)
tk.Button(mainfrm, height=30, width=30, bitmap="info").place(x=130, y=60)
tk.Button(mainfrm, height=30, width=30, bitmap="question").place(x=170, y=60)
tk.Button(mainfrm, height=30, width=30, bitmap="warning").place(x=210, y=60)

mainfrm.mainloop()