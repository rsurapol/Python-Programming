for i in range(1, 6):
    n = int(input("กรุณาป้อนคัวเลข 1-10 : "))
    if n >= 11:
        print ("คุณป้อนตัวเลขไม่ถูกต้อง !!")
        break
    if n <= 10:
        j = n * i
    print ("ผลคูณระหว่าง %d x %d = " %(i, n), j)
print ("สิ้นสุดการทำงานของโปรแกรม")