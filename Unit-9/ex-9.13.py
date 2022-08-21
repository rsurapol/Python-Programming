try:
    n = int(input("กรุณากรอกคะแนนไม่เกิน 30 คะแนน : "))
    assert n < 30
    print ("คะแนนที่คุณกรอก คือ ", n)
except ValueError:
    print ("คุณป้อนค่าตัวเลขไม่ถูกต้อง")
except AssertionError:
    print ("คุณป้อนค่าตัวเลขเกินจำนวน")