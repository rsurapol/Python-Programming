money = int(input("กรุณาป้อนจำนวนเงิน = "))
if money >= 30000:
    if money <= 35000:
        print("Buy = Iphone7")
    else:
        print ("Buy = Iphone7plus")
elif money >= 20000:
    if money <= 25000:
        print ("Buy = Galaxy s7")
    else:
        print ("Buy = Galaxy s8")
else:
    print ("Buy = Oppo")