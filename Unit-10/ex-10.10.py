file = open(r"D:\PythonFiles\NewFile.txt","rb+")
file.seek(-5, 2)
print (file.read())
file.close()