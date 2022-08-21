books_set = {"Python", "PHP", "Java", "Scala"}
books_set1 = {"C", "C++", "C#", "Java", "Python"}
books_set2 = {"Python", "PHP", "Java", "Scala", "C"}
books_inter = books_set.intersection(books_set1, books_set2)
books_inter1 = books_set1 & books_set2
print ("ผล intersection จาก books_inter =", books_inter)
print ("ผล intersection จาก books_inter1 =", books_inter1)
print ("ผล books_set & books_set2 =", books_set & books_set2)