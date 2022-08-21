from tkinter import *
from tkinter import ttk

mainfrm = Tk()

def calculate():
    num1 = entNum1.get()
    num2 = entNum2.get()
    if chkAdd.instate(["selected"]):
        result = int(num1) + int(num2)
        entResult.insert("", str(result))
    elif chkSub.instate(["selected"]):
        result = int(num1) - int(num2)
        entResult.insert("", str(result))
    elif chkMulti.instate(["selected"]):
        result = int(num1) * int(num2)
        entResult.insert("", str(result))
    elif chkDivide.instate(["selected"]):
        result = int(num1) / int(num2)
        entResult.insert("", str(result))

def clearEntry():
    entNum1.delete(0, END)
    entNum2.delete(0, END)
    entResult.delete(0, END)

lblFrm1 = ttk.LabelFrame(mainfrm, text="โปรแกรมคำนวณ", labelanchor="n")
lblFrm1.pack(padx=10, pady=10, side="left")

lblNum1 = ttk.Label(lblFrm1, text="ป้อนตัวเลขที่ 1 :").grid(column=0, row=0, padx=5, sticky="e")
lblNum2 = ttk.Label(lblFrm1, text="ป้อนตัวเลขที่ 2 :").grid(column=0, row=1, padx=5, sticky="e")
lblResult = ttk.Label(lblFrm1, text="ผลลัพธ์ :").grid(column=0, row=2, padx=5, sticky="e")

entNum1 = ttk.Entry(lblFrm1)
entNum2 = ttk.Entry(lblFrm1)
entResult = ttk.Entry(lblFrm1)

entNum1.grid(column=1, row=0, padx=5)
entNum2.grid(column=1, row=1, padx=5)
entResult.grid(column=1, row=2, padx=5)

btnEnter = ttk.Button(lblFrm1, text="Enter", command=calculate).grid(column=0, row=3, padx=5, pady=5)
btnClear = ttk.Button(lblFrm1, text="Clear", command=clearEntry).grid(column=1, row=3, padx=5, )

lblFrm2 = ttk.LabelFrame(mainfrm, text="เลือกการคำนวณ", labelanchor="n")
lblFrm2.pack(padx=10, pady=10)

chkAdd = ttk.Checkbutton(lblFrm2, text="การบวก")
chkSub = ttk.Checkbutton(lblFrm2, text="การลบ")
chkMulti = ttk.Checkbutton(lblFrm2, text="การการคูณ")
chkDivide = ttk.Checkbutton(lblFrm2, text="การหาร")

chkAdd.state(["!alternate"])
chkSub.state(["!alternate"])
chkMulti.state(["!alternate"])
chkDivide.state(["!alternate"])

chkAdd.grid(column=0, row=0, sticky="w")
chkSub.grid(column=0, row=1, sticky="w")
chkMulti.grid(column=0, row=2, sticky="w")
chkDivide.grid(column=0, row=3, sticky="w")

mainfrm.mainloop()