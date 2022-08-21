import tkinter as tk
from tkinter import ttk, messagebox

mainfrm = tk.Tk()
def msg():
    msg = tk.messagebox.showwarning("Warning", "Out of memory")
btn = ttk.Button(mainfrm, text="Click", command=msg, width=10)
btn.pack(padx=10, pady=10)

mainfrm.mainloop()