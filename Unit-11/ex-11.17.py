import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", passwd="1234",
                          db="register", charset="utf8")
    cs = con.cursor()
    cs.execute("DROP TABLE registers")

    con.commit()
    con.close()
    cs.close()
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง !!!")
    con.rollback()
except:
    print("ไม่ปรากฎตารางที่ต้องการลบ")
else:
    print("ลบตารางออกจากฐานข้อมูลเรียบร้อยแล้ว !!!")