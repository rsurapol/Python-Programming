import pymysql

try:
    con = pymysql.connect(host="localhost", user="root",
                          passwd="1234", db="register")
    cs = con.cursor()

    cs.execute("""CREATE TABLE students (student_id INT(5) NOT NULL, 
                f_name CHAR(30) COLLATE utf8_bin, 
                l_name CHAR(30) COLLATE utf8_bin,
                e_mail VARCHAR(30) COLLATE utf8_bin,
                tel VARCHAR(10) COLLATE utf8_bin, 
                PRIMARY KEY(student_id))""")

    cs.execute("""CREATE TABLE teachers (teacher_id INT(3) NOT NULL, 
                f_name CHAR(30) COLLATE utf8_bin, 
                l_name CHAR(30) COLLATE utf8_bin,
                e_mail VARCHAR(30) COLLATE utf8_bin,
                tel VARCHAR(10) COLLATE utf8_bin, 
                PRIMARY KEY(teacher_id))""")

    cs.execute("""CREATE TABLE subjects (subject_id INT(3) NOT NULL, 
                subject_name CHAR(50) COLLATE utf8_bin, 
                unit INT(1),
                teacher_id INT(3), 
                PRIMARY KEY(subject_id))""")

    cs.execute("""CREATE TABLE registers (student_id INT(5) NOT NULL, 
                subject_id INT(3) NOT NULL,
                semester INT(1) NOT NULL,
                register_date DATE, 
                PRIMARY KEY(student_id, subject_id, semester))""")

except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง !!!")
else:
    print("สร้างตารางเรียบร้อยแล้ว !!!")
    con.close()
    cs.close()