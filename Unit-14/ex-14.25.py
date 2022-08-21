import tkinter as tk

frame = tk.Tk()
lblfrm = tk.LabelFrame(frame, text="Countries", padx=5, pady=5)
lblfrm.pack()

lbCoun = tk.Listbox(lblfrm, height=5)
lbCoun.insert(1, "Australia")
lbCoun.insert(2, "Belize")
lbCoun.insert(3, "Colombia")
lbCoun.insert(4, "Sweden")
lbCoun.insert(5, "Thailand")
lbCoun.pack()

frame.mainloop()