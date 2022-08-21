a = 5; b = 3; c = 15; z = 0

z = a == b and c < b
print("ผลลัพธ์ของ a == b and c < b คือ ", z)
z = a > b and a < c
print("ผลลัพธ์ของ a > b and a < c คือ ", z)
z = b > a or a > c
print("ผลลัพธ์ของ b > a or a > c คือ ", z)
z = b < a or c > a
print("ผลลัพธ์ของ b < a or c > a คือ ", z)
z = not (a < c)
print("ผลลัพธ์ของ not (a < c) คือ ", z)
z = not (b > a or c < a)
print("ผลลัพธ์ของ not (b > a or c < a) คือ ", z)