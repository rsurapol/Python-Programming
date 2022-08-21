def msg(f_lst):
    print ("ค่่าพารามิเตอร์ที่รับมาจาก arg_lst =", f_lst)
    f_lst[0] = "Python is a powerful programming language."
    print ("เปลี่ยนค่าพารามิเตอร์ = ", f_lst)

arg_lst = ["Python is easy to learn."]
print ("ค่าอาร์กิวเมนต์ที่ส่งให้ค่าพารามิเตอร์ =", arg_lst)
msg(arg_lst)
print ("ค่าอาร์กิวเมนต์หลังจากเปลี่ยนค่าพารามิเตอร์ =", arg_lst)