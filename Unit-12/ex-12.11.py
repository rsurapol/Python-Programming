def varleng_arg(*num):
    print("จำนวนข้อมูลในตัวแปร num :")
    for var in num:
        print(var, end=" ")
    print(" ")
    result = num[2] * 2
    print("ผลคูณพารามิเตอร์ num[2] * 2 =", result)

varleng_arg(10, 20, 30, 40)