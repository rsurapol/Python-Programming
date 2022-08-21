file = open(r"D:\PythonFiles\ProLang.txt","r")
for data in range(6):
    print (next(file, "End !!!"))
file.close()