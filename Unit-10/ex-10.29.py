import csv

with open(r"D:\PythonFiles\Fruits.csv", "w+", newline="") as file:
    csvfile = csv.writer(file)
    csvfile.writerow(["Apple", "Mango", "Watermelon"])
    csvfile.writerow(["Banana", "Lime", "Orange"])
    csvfile.writerow(["Grapes", "Coconut", "Lemon"])