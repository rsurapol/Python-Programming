while True:
    i = input("ต้องการป้อนคะแนนให้กด Y ออกจากโปรแกรมให้กด N : ")
    print ("-----------------------------------------------")
    if i == "N":
        break
    elif i == "Y":
        n = int(input("นักเรียนคนที่ = "))
        j = 1
        lst = []
        while j <= 3:
            score = float(input("กรอกคะแนนครั้งที่ %d = " %j))
            lst.append(score)
            j += 1
        print ("นักเรียนคนที่ %d ได้คะแนน = " %n, lst, "คะแนนรวม =", sum(lst))
        print("----------------------------------------------------------")
print ("สิ้นสุดการทำงานของโปรแกรม")