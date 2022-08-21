import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", passwd="1234",
                          db="register", charset="utf8")
    cs = con.cursor()
    cs.execute("SELECT * FROM students")

except pymysql.err.OperationalError:
    print ("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print ("คำสั่ง SQL ไม่ถูกต้อง !!!")
else:
    data = cs.fetchone()
    print (data)
    con.close()
    cs.close()