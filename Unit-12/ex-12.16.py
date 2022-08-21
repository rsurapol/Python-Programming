def circle_area():
    global r; r = 10
    global pi; pi = 3.14
    result = pi * (r * r)
    return result
def circumference():
    result = 2 * pi * r
    return result
print ("พื้นที่วงกลม = ", circle_area(), "ตารางเมตร")
print ("เส้นรอบวงวงกลม = %.3f" %circumference(), "เมตร")