n = int(input("ป้อนตัวเลข 1-5 : "))
if n > 5:
    raise TypeError("คุณป้อนค่าตัวเลขมากกว่าที่กำหนด", n)
else:
    print("จบการทำงาน !!")