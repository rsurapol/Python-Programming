file = open(r"D:\PythonFiles\NewFile.txt","r")
file.seek(10)
print (file.read())
file.close()