books_set = {"Python", "PHP", "Java", "Scala"}
books_set1 = {"C", "C++", "C#", "Java", "Python"}
books_differ = books_set.difference(books_set1)
books_differ1 = books_set1 - books_set
print ("สมาชิกใน books_set แตกต่างจาก books_set1 คือ", books_differ)
print ("สมาชิกใน books_set1 แตกต่างจาก books_set คือ", books_differ1)