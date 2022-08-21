def bonus_1(m, ot):
    total =  (m + (ot * 20)) * 0.5
    salary = total + m
    return salary
def bonus_2(m, ot):
    total =  (m + (ot * 20)) * 0.2
    salary = total + m
    return salary

print ("เงินเดือนที่ได้รับสุทธิ = ", bonus_1(12000, 5), "บาท")
print ("เงินเดือนที่ได้รับสุทธิ = ", bonus_2(20000, 5), "บาท")