name = str(input("ชื่อพนักงาน = "))
salary = int(input("เงินเดือน = "))
OT = int(input("จำนวนชั่วโมงที่ทำงานล่วงเวลา = "))
cal_ot = OT * 20
bonus = salary * 0.5
ot_bonus = cal_ot + bonus
salary_total = salary + ot_bonus
print ("ค่าทำงานล่วงเวลา %d * 20  = %.2f" %(OT,cal_ot), "บาท")
print ("ค่า bonus %d * 0.5 = %.2f" %(salary,bonus), "บาท")
print ("รวม OT และ bonus %.2f + %.2f = %.2f" %(cal_ot,bonus,ot_bonus),"บาท")
print ("รายได้สุทธิ %d + %.2f = %.2f" %(salary,ot_bonus,salary_total), "บาท")