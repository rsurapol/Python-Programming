msg = "Python is easy programming language to learn."
file = open(r"D:\PythonFiles\NewFile.txt","w")
file.write(msg)
file.flush()
file.close()