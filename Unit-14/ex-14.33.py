from tkinter import *
from tkinter import ttk

mainfrm = Tk()
lblfrm = ttk.LabelFrame(mainfrm, text="Programming Language")
lblfrm.pack(padx=10, pady=10)

rdoPy = ttk.Radiobutton(lblfrm, text="Python").grid(column=0,row=0, sticky="w", padx=20)
rdoR = ttk.Radiobutton(lblfrm, text="R").grid(column=0,row=1, sticky="w", padx=20)
rdoSc = ttk.Radiobutton(lblfrm, text="Scala").grid(column=0,row=2, sticky="w", padx=20)
rdoJa = ttk.Radiobutton(lblfrm, text="Java").grid(column=0,row=3, sticky="w", padx=20)

mainfrm.mainloop()