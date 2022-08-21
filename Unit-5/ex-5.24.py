num_tup_1 = (4, 5, 7, -5.12, -10, 15)
num_tup_2 = (4, 5, 4.12, 7,)
num_tup_3 = (4, 5, 4.12, 7,)
books_tup_1 = ("Python", "Java", "C", "C++", "C#")
books_tup_2 = ("C", "C++", "C#")
less_than = num_tup_1 < num_tup_3
equal_ = num_tup_2 == num_tup_3
merge = books_tup_1 + books_tup_2
dup = books_tup_1 * 2
print ("ผลเปรียบเทียบ num_tup_1 < num_tuple_3 คือ", less_than)
print ("ผลเปรียบเทียบ num_tup_1 = num_tuple_3 คือ",  equal_)
print ("ผลการวมระหว่าง books_tup_1 กับ books_tuple_2 คือ",  merge)
print ("ผลการคูณของ books_tup_1 คือ", dup)