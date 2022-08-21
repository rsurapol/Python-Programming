data = b"Python is easy to learn."
file = open(r"D:\PythonFiles\Binary.txt","wb")
file.write(data)
file.close()

file = open(r"D:\PythonFiles\Binary.txt", "rb").read()
print (file)