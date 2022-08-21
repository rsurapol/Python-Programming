import pymysql

con = pymysql.connect(host="localhost", user="root", passwd="1234", db="")
cs = con.cursor()
cs.execute("show databases")
sv = cs.fetchone()
print ("%s" %sv)
con.close()
cs.close()