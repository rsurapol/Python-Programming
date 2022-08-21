books_set = {"Python", "PHP", "Java", "Scala", ".NET"}
books_set1 = {"C", "C++", "C#", "HTML","R"}
books_set2 = {"Java", "Scala", ".NET"}
books_sup = books_set.issuperset(books_set1)
books_sup1 = books_set.issuperset(books_set2)
print ("books_set เป็น superset ของ books_sets1 =", books_sup)
print ("books_set เป็น superset ของ books_sets2 =", books_sup1)