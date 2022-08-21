import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", passwd="1234")
    cs = con.cursor()
    cs.execute("DROP DATABASE register")

    con.close()
    cs.close()
except pymysql.err.OperationalError:
    print("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print("คำสั่ง SQL ไม่ถูกต้อง !!!")
except:
    print("ไม่ปรากฎฐานชื่อข้อมูลที่ต้องการลบ")
else:
    print("ลบฐานข้อมูลเรียบร้อยแล้ว !!!")