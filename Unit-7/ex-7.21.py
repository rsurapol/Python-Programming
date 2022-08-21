nums_set = {4, 3, 2, 5, 9}
nums_set1 = {1, 4, 5, 2, 7}
nums_set2 = {1, 5, 7, 6, 8}
n = nums_set.union(nums_set1)
n1 = nums_set1 | nums_set2
print ("union ระหว่าง nums_set กับ nums_set1 =", n)
print ("union ระหว่าง nums_set1 กับ nums_set2 =", n1)