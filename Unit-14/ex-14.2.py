from tkinter import *
from tkinter import ttk

mainFrm = Tk()
mainFrm.title("โปรแกรมบวกเลข")

lblTitle = ttk.Label(mainFrm, text="โปรแกรมบวกเลข", font='20')
lblNum1 = ttk.Label(mainFrm, text="ป้อนตัวเลขที่ 1 :")
lblNum2 = ttk.Label(mainFrm, text="ป้อนตัวเลขที่ 2 :")
lblTotal = ttk.Label(mainFrm, text="ผลลัพธ์ :")

lblTitle.grid(column=0, columnspan=2, padx = 150, pady=10)
lblNum1.grid(column=0, row=2, pady=5, sticky="NE")
lblNum2.grid(column=0, row=3, pady=5, sticky="NE")
lblTotal.grid(column=0, row=4, pady=5, sticky="NE")

entNum1 = ttk.Entry(mainFrm, width=25).grid(column=1, row=2, sticky="W")
entNum2 = ttk.Entry(mainFrm, width=25).grid(column=1, row=3, sticky="W")
entTotal = ttk.Entry(mainFrm, width=25).grid(column=1, row=4, sticky="W")

btnClick = ttk.Button(mainFrm, text="Click", width=10)
btnClear = ttk.Button(mainFrm, text="Clear", width=10)

btnClick.grid(column=0, row=5, pady=10, sticky="NE")
btnClear.grid(column=1, row=5, padx=10, sticky="W")

mainFrm.mainloop()