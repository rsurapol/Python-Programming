try:
    n = int(input("กรุณาป้อนตัวเลขจำนวนเต็ม : "))
    try:
        x = 10
        z = x / n
        print (z)
    except ZeroDivisionError:
        print ("ไม่สามารถหารด้วยเลข 0")
except ValueError:
    print ("คุณป้อนข้อมูลไม่ถูกต้อง")