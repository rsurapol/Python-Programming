import os # import ไลบรารี os
print (os.getcwd())  # แสดงตำแหน่งไดเรกทอรีที่เริ่มต้นทำงาน
os.chdir(r"D:\PythonFiles\MyDirectory") # เปลี่ยนตำแหน่งไดเรกทอรีใหม่
print (os.getcwd())  # แสดงตำแหน่งไดเรกทอรีที่ทำงานใหม่