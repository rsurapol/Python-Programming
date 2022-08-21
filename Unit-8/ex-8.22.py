salary = int(input("ป้อนเงินเดือนพนักงาน = "))
if salary <= 30000:
    pass
elif salary <= 35000:
    pass
elif salary <= 40000:
    bonus = salary * 3
    print ("เงินโบนัส =", bonus, "บาท")
else:
    bonus = salary * 2
    print ("เงินโบนัส =", bonus, "บาท")
print ("สิ้นสุดการทำงานของโปรแกรม")