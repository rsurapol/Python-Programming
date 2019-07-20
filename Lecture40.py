#!/usr/bin/env python
# coding: utf-8

# In[2]:


if True:
    print("Hello Welcome")
    if True:
        print("Yo! Mister A")
        if True:
            print("Ha Ha")


# In[8]:


usernameinput = input("Username : ")
passwordinput = input("Password : ")
if usernameinput == "admin" and passwordinput == "1234" :
    print("Done !")
    print("---------------iShop---------------")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB) : "))
        vat = 7
        result = price + (price * vat / 100)
        print(result)
    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print(price1+price2)


# In[10]:


username = input("Username : ")

password = input("Password : ")

if username == "admin" and password == "1234" :

    print("Welcome to my shop!!!")

    print("---Please selecting product---")

    print("1.chair 50 THB")

    print("2.table 100 THB")

    selected = int(input("Select number : "))

    if selected == 1:

        print("How many do you want?")

        chair = 50

        amount = int(input("I want : "))

        total = chair*amount

        print("Total price :",total,"THB")

    elif selected == 2:

        print("How many do you want?")

        table = 100

        amount = int(input("I want : "))

        total = table*amount

        print("Total price :",total,"THB")

    else :

        print("ERROR")

else :

    print("Username or Password incorrect")


# In[ ]:




