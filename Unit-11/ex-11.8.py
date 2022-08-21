import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", passwd="1234",
                          db="register", charset="utf8")
    cs = con.cursor()
    cs.execute("""INSERT INTO registers(student_id, subject_id, semester, register_date)
                VALUES(10001, 101, 1, 20160710)""")

except pymysql.err.OperationalError:
    print ("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print ("คำสั่งเพิ่มข้อมูลผิดพลาด !!!")
    con.rollback()
else:
    con.commit()
    print ("บันทึกข้อมูลเรียบร้อยแล้ว !!!")
    con.close()
    cs.close()