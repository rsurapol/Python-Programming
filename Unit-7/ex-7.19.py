nums_set = {4, 3, 2, 5, 9}
nums_set1 = {1, 4, 5, 2, 7}
nums_set2 = {1, 5, 7, 6, 8}
n = nums_set.symmetric_difference(nums_set1)
n1 = nums_set1.symmetric_difference(nums_set2)
n2 = nums_set ^ nums_set2
print ("nums_set และ numset1 มีสมาชิกที่ต่างกัน คือ", n)
print ("nums_set1 และ numset2 มีสมาชิกที่ต่างกัน คือ",n1)
print ("nums_set และ numset2 มีสมาชิกที่ต่างกัน คือ",n2)