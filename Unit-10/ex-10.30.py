import csv

file = csv.reader(open(r"D:\PythonFiles\Fruits.csv", "r"))
for data in file:
    print ("{}, {}, {}".format(data[0], data[1], data[2]))