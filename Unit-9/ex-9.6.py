x = [5, 12, 6, 9, 13]
try:
    n = int(input("กรุณาป้อนตัวเลข : "))
    z = x[7]/n
except IndexError:
    print ("ไม่พบตำแหน่งที่คุณระบุในลิสต์ x")
except ArithmeticError:
    print ("ตัวหารเป็นเลข 0")
except ValueError:
    print ("ข้อมูลที่คุณป้อนไม่ใช่ตัวเลข")
else:
    print("ไม่พบข้อผิดพลาดของ Exception")
    print ("ผลลัพธ์ที่ได้ =", z)