import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", passwd="1234",
                          db="register", charset="utf8")
    cs = con.cursor()
    cs.execute("""SELECT subject_name, f_name, l_name  
                    FROM subjects, teachers
                    WHERE subjects.teacher_id = teachers.teacher_id""")

except pymysql.err.OperationalError:
    print ("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print ("คำสั่ง SQL ไม่ถูกต้อง !!!")
else:
    data = cs.fetchall()
    for (subject_name, f_name, l_name) in data:
        print("{:25} {} {}".format(subject_name, f_name, l_name))
    con.close()
    cs.close()