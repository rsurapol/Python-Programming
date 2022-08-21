nums_set = {4, 3, 2, 5, 9}
nums_set1 = {1, 4, 5, 2, 7}
nums_set2 = {1, 5, 7, 6, 8}
nums_set.symmetric_difference_update(nums_set1)
nums_set1.symmetric_difference_update(nums_set2)
print ("สมาชิกใน nums_set คือ", nums_set)
print ("สมาชิกใน numset1 คือ",nums_set1)