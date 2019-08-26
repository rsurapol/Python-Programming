H = int(input("H: "))
U = int(input("U: "))
D = int(input("D: "))
k = 0
day = 1
while True:
   k = k+U
   if k>=H:
      break
   k = k-D
   day = day+1
print(day,"day(s).")