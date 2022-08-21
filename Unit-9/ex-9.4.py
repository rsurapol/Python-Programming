x =5
try:
    n = int(input("กรุณาป้อนตัวเลข: "))
    z = x/n
    print (z)
except ZeroDivisionError:
    print("ไม่สามารถหารด้วย 0 ได้")
except ValueError:
    print("ข้อมูลที่คุณป้อนไม่ใช่ตัวเลข")