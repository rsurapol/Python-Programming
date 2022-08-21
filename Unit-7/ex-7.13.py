books_set = {"Python", "PHP", "Java", "Scala", ".NET"}
books_set1 = {"C", "C++", "C#", "HTML","R"}
books_set2 = {".NET", "PHP", "C#", "Python"}
books_isd = books_set.isdisjoint(books_set1)
books_isd1 = books_set.isdisjoint(books_set2)
print ("books_set มีสมาชิกซ้ำกับ books_sets1 =", books_isd)
print ("books_set มีสมาชิกซ้ำกับ books_sets2 =", books_isd1)