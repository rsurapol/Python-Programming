s = "Python"
l = [10, 11, 20, 1, 14, 3]
t = ("Python", "๋Java", "PHP", "C", "C++", "C#")
print(list(reversed(s)))
print(list(reversed(l)))
for i in reversed(t):
    print(i, end= " ")