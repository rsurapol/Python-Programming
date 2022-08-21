import tkinter as tk
mainframe = tk.Tk()
mainframe.title("Main Frame")

tp = tk.Toplevel()
tp.title("Toplevel Frame")
lbl = tk.Label(tp, text="This is Toplevel widget.")
lbl.pack(padx=50, pady=50)

mainframe.mainloop()