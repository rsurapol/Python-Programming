count = int(input("How many books: "))
money = int(input("How much: "))
if count > 3 and money > 500:
   s = money-money*0.1
else:
   s = money
print("You have to pay",int(s),"bath.")