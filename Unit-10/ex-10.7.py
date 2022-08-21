# เปิดไฟล์ขึ้นมาเขียนด้วยโหมด w+ ด้วยคำสั่ง with
with open(r"D:\PythonFiles\WriteWithFile.txt", "w+") as file:
    file.write("Python is easy to learn.") # เขียนข้อความลงไฟล์