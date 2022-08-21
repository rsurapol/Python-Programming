i = 1
while i <= 5:
    n = int(input("กรุณาป้อนคัวเลข 1-10 : "))
    if n >= 11:
        print ("คุณป้อนตัวเลขไม่ถูกต้อง !!")
        continue
    if n <= 10:
        j = n * i
    print ("ผลคูณระหว่าง %d x %d = " %(i, n), j)
    i += 1