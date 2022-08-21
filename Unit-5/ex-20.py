nums_lst = [4, 5, 4.12, 7, -5.12, 15]
nums_lst1 = [4, 3, 5, -9, -45, 78]
books_lst = ["Python", "Java", "C", "C++", "C#", "Scala" ]
print (nums_lst + books_lst)
print (nums_lst * 3)
print ("เปรียบเทียบ num_lst กับ nums_lst1 เท่ากันหรือไม่ = ", nums_lst == nums_lst1)
news_lst = [nums_lst, books_lst]
print (news_lst)
print ("ค้นหาหนังสือภาษา Python ใน books_list =", "Python" in books_lst)