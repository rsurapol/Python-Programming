books_set = {"Python", "PHP", "Java", "Scala", ".NET"}
books_set1 = {"C", "C++", "C#", "HTML","R"}
books_set2 = {"Java", "Scala", ".NET"}
books_sub = books_set.issubset(books_set1)
books_sub1 = books_set2.issubset(books_set)
print ("books_set เป็น subset ของ books_set1 =", books_sub)
print ("books_set2 เป็น subset ของ books_set =", books_sub1)