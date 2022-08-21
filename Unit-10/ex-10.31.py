import csv

with open(r"D:\PythonFiles\ProLang.csv", "w+", newline="") as csvfile:
    prolang = csv.writer(csvfile, delimiter ="\t")
    prolang.writerow(["Jave", "C", "C#"])
    prolang.writerow(["HTML", "PHP", ".NET"])
    prolang.writerow(["Python", "R", "Scala"])