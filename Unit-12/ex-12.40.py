s = "Python Programming"
s_slice = slice(1, 5)
print("ค่าข้อมูลตำแหน่งที่ 1-5 =",s[s_slice])
print("ค่าข้อมูลตำแหน่งที่ 1-10 ข้ามครั้งละ 2 ตำแหน่ง =", s[slice(1, 10, 2)])