i = 1
num =[]
while i <= 5:
    n = int(input("ป้อนตัวเลขจำนวน ครั้งที่ %d = " %i))
    num.append(n)
    i = i + 1
print ("ตัวเลขที่คุณป้อน = %s" %num)
print ("ตัวเลขค่าที่น้อยที่สุด = ", min(num))
print ("ตัวเลขค่าที่มากที่สุด = ", max(num))
print ("ผลบวกตัวเลขทั้งหมด = ", sum(num))