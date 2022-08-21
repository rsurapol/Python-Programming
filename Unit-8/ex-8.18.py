stu = int(input("ป้อนจำนวนนักเรียน = "))
for i in range(1, stu + 1):
    j = 1
    lst = []
    print ("นักเรียนคนที่ ", i)
    while j <= 3:
        n = float(input("กรอกคะแนนครั้งที่ %d = " %j))
        lst.append(n)
        j += 1
    if sum(lst) <= 49:
        print ("นักเรียนคนที่ %d ได้คะแนน = " %i, lst, "คะแนนรวม =", sum(lst), "เกรด = F")
    elif sum(lst) <= 59:
        print ("นักเรียนคนที่ %d ได้คะแนน = " %i, lst, "คะแนนรวม =", sum(lst), "เกรด = D")
    elif sum(lst) <= 69:
        print ("นักเรียนคนที่ %d ได้คะแนน = " %i, lst, "คะแนนรวม =", sum(lst), "เกรด = C")
    elif sum(lst) <= 79:
        print ("นักเรียนคนที่ %d ได้คะแนน = " %i, lst, "คะแนนรวม =", sum(lst), "เกรด = B")
    else:
        print ("นักเรียนคนที่ %d ได้คะแนน = " %i, lst, "คะแนนรวม =", sum(lst), "เกรด = A")