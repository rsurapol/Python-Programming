data = ["Python\n", "C++\n", "C#\n", "Scala\n"] # สร้างข้อความแบบ sequence
file = open(r"D:\PythonFiles\SeqFile.txt","w") # เปิดไฟล์ขึ้นมาอ่านด้วยโหมด w
file.writelines(data) # เขียนข้อความลงไฟล์
file.flush() # บันทึกข้อความลงไฟล์
file.close() # ปิดไฟล์