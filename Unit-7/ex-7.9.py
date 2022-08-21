books_set = {"Python", "PHP", "Java", "Scala", ".NET"}
books_set1 = {"C", "C++", "C#", "Java", "Python"}
books_set2 = {".NET", "PHP", "C#", "Python"}
books_up = books_set.difference_update(books_set1)
books_up1 = books_set.difference(books_set2)
print ("สมาชิกที่มีอยู่ใน books_set คือ", books_set)
print ("สมาชิกที่อยู่ใน books_set ต่างจาก books_sets2 คือ", books_up1)
print ("สมาชิกที่มีอยู่ใน books_set คือ", books_up)