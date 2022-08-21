import pymysql

try:
    con = pymysql.connect(host="localhost", user="root", passwd="1234")
    cs = con.cursor()
    cs.execute("CREATE DATABASE register")
except pymysql.err.OperationalError:
    print ("ไม่สามารถติดต่อฐานข้อมูลได้ !!!")
except pymysql.err.ProgrammingError:
    print ("คำสั่ง SQL ไม่ถูกต้อง !!!")
else:
    print ("สร้างฐานข้อมูลเรียบร้อยแล้ว !!!")
    con.close()
    cs.close()