sports = ["Running", "Swimming", "Tennis", "Racing", "Football"]
i=0
for sport in range(len(sports)):
    print("ชื่อชนิดกีฬาตำแหน่งที่ %d คือ" %(i),sports[sport])
    i = i+1
else:
    print("Done !!")