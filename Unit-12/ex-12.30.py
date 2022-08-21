lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filter_lst(lst1):
    lst_f = (1, 3, 5, 7, 9)
    if(lst1 in lst_f):
        return True
    else:
        return False
lst_f = filter(filter_lst, lst1)
for vowel in lst_f:
    print(vowel, end = " ")