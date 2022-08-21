nums_set = {4, 3, 2, 5, 9}
nums_set1 = {4, 3, 2, 9}
nums_set2 = {3, 4, 2, 5, 9}
nums_set3 = {8, 4, 2, 5, 9}
eq_set = nums_set == nums_set1
le_set = nums_set1 < nums_set2
in_set = 4 in nums_set3
is_set = nums_set is nums_set3
print ("nums_set เท่ากับ num_set1 หรือไม่่ =", eq_set)
print ("nums_set1 น้อยกว่า num_set2 หรือไม่่ =", le_set)
print ("4 เป็นสมาชิกของ nums_set3 หรือไม่ =", in_set)
print ("nums_set เท่ากับ nums_set3 หรือไม่ =", is_set)