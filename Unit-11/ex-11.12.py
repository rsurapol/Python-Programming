import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", passwd="1234",
                          db="register", charset="utf8")
    cs = con.cursor()
    cs.execute("SELECT * FROM subjects where teacher_id = 101")

except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง !!!")
else:
    print("{:<15}{:<20}{:<10}{}".format("subject_id", "subject_name", "unit", "teacher_id"))
    data = cs.fetchall()
    for (subject_id, subject_name, unit, teacher_id) in data:
        print("{:<15}{:<20}{:<10}{}".format(subject_id, subject_name, unit, teacher_id))
    con.close()
    cs.close()