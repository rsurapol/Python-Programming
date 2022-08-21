def maplist(x, y):
    return x + y

t = (4, 5, 6, 7)
l = [7 ,8, 9, 4]
result = map(maplist, t, l)
for i in result:
    print(i, end=" ")