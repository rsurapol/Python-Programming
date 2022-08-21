cash = int(input("ป้อนจำนวนเงิน : "))
vat = 0.07
total = cash - (cash * vat)
def cash(cash):
    total = cash - (cash * vat)
    return total
print ("ชำระเป็นจำนวนเงิน = ", cash(5000), "บาท")
print ("ชำระเป็นจำนวนเงิน = ", total, "บาท")