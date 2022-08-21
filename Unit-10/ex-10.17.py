file = open(r"D:\PythonFiles\NewFile.txt", "w+")
file.write("Python is esay to learn.") # ข้อความที่จะถูกเขียน
file.truncate(15) # เขียนข้อความลงไฟล์ 15 ตัวอักขระ
file.close() # ปิด
# แสดงผลข้อความในไฟล์
file = open(r"D:\PythonFiles\NewFile.txt", "r")
print (file.read())
file.close()