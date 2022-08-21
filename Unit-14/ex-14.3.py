from tkinter import *
from tkinter import ttk

mainfrm = Tk()
mainfrm.title("การจัดตำแหน่งด้วยเมธอด grid()")

ttk.Label(mainfrm, text="ชื่อ :").grid(column=0, row=0, padx=2, pady=2, sticky="e")
ttk.Label(mainfrm, text="นามสุกล :").grid(column=0, row=1, padx=2, pady=2, sticky="e")
ttk.Label(mainfrm, text="ที่อยู่ :").grid(column=0, row=2, padx=2, pady=2, sticky="e")

ttk.Entry(mainfrm).grid(column=1, row=0)
ttk.Entry(mainfrm).grid(column=1, row=1)
ttk.Entry(mainfrm).grid(column=1, row=2)

ttk.Label(mainfrm, text="เพศ:").grid(column=2, row=0, columnspan=2)
ttk.Checkbutton(mainfrm, text="ชาย").grid(column=2, row=1, padx=20)
ttk.Checkbutton(mainfrm, text="หญิง").grid(column=3, row=1,  padx=20)

ttk.Button(mainfrm, text="ลงทะเบียน").grid(column=1, row=3, pady=10)
ttk.Button(mainfrm, text="ยกเลิก").grid(column=2, row=3, pady=10)

mainfrm.mainloop()