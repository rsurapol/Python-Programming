import tkinter as tk

frame = tk.Tk()

msg = tk.Message(frame, text="Out of memory", relief="groove", padx=50, pady=15, width=100)
msg.grid(column=0, row=0, padx=80, pady=20)

frame.mainloop()