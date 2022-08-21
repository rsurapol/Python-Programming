lst = [5, 6, 8, 9, 10, 15]
dct = {1:"Tennis", 2:"Football", 3:"Racing", 4:"Running"}
try:
    print ("ตำแหน่งที่ 5 ของ lst =", lst[5])
    print ("ตำแหน่งที่ 2 ของ dct =", dct[6])
except(IndexError, KeyError):
    print ("ตำแหน่ง หรือ คีย์ที่ระบุไม่ถูกต้อง")