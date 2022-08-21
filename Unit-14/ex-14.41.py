from tkinter import *
from tkinter import ttk

mainfrm = Tk()

trv = ttk.Treeview(mainfrm)
trv.insert("", 0, "linuxOS", text="Linux")
trv.insert("linuxOS", 0, text="CentOS")
trv.insert("linuxOS", 1, text="RedHad")
trv.insert("linuxOS", 2, text="Ubuntu")
trv.insert("", 1, "winOS", text="Windows")
trv.insert("winOS", 0, text="Windows 7")
trv.insert("winOS", 1, text="Windows 8")
trv.insert("winOS", 2, text="Windwos 10")
trv.pack()

mainfrm.mainloop()