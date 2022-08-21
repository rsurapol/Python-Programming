r = int(input("ป้อนค่ารัศมี : "))
h = int(input("ป้อนค่าความสูง : "))
def cylinder():
    area = 3.14 * (r * r) * h
    return area
print ("ปริมาตรทรงกระบอก = ", cylinder(), "ตารางเมตร")