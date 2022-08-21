import tkinter as tk
from tkinter import filedialog

mainframe = tk.Tk()
def openfile():
    tk.filedialog.askopenfilename()
btn = tk.Button(mainframe, text="OpenFile", command=openfile, width=10)
btn.pack(padx=10, pady=10)

mainframe.mainloop()