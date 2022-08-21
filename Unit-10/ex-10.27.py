header = ("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}\n".format("Students","Score",\
                                                   "MidTerm ","Final","Total ", "Grade"))
file = open(r"D:\PythonFiles\Score.txt", "a", encoding = "utf-8")
file.write(header)
j = 0
stu = int(input("ป้อนจำนวนนักเรียน = "))
while j < stu:
    stuID = int(input("รหัสนักศึกษา = "))
    score = float(input("ป้อนคะแนนเก็บ = "))
    midterm = float(input("ป้อนคะแนนกลางภาค = "))
    final = float(input("ป้อนคะแนนปลายภาค = "))
    total = score + midterm + final
    if total < 50:
        grade = "F"
    elif total < 60:
        grade = "D"
    elif total < 70:
        grade = "C"
    elif total < 80:
        grade = "B"
    else:
        grade = "A"
    print ("StudentID = ", stuID, "Score = ", score, "Midterm = ", midterm,\
           "Final = ", final, "Total = ", total, "Grad = ", grade)
    file.write("{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}\n".format(stuID, score,\
                                                       midterm, final,total,grade))
    j += 1
file.close()