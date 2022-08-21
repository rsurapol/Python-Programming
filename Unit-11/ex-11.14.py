import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", passwd="1234",
                          db="register", charset="utf8")
    cs = con.cursor()
    cs.execute("""SELECT students.student_id, students.f_name, students.l_name, 
                    subjects.subject_id, subjects.subject_name, registers.semester
                    FROM students, subjects, registers
                    WHERE registers.student_id = students.student_id AND 
                    registers.subject_id = subjects.subject_id AND 
                    semester = 1""")

except pymysql.err.OperationalError:
    print ("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print ("คำสั่ง SQL ไม่ถูกต้อง !!!")
else:
    data = cs.fetchall()
    for (st_id, st_f, st_l, sub_id, sub_name, year) in data:
        print("{}, {} {}, {}, {}, {}".format(st_id, st_f, st_l, sub_id, sub_name, year))
    print (" ")
    print("จำนวนทั้งหมด =", cs.rowcount, "รายการ")
    con.close()
    cs.close()