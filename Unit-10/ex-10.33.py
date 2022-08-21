import json

with open(r"D:\PythonFiles\teachers.json", "r") as file:
    data = json.load(file)
    for row in data["teachers"]:
        print ("{:5} {:10} {:10} {:20} {}".format(row["teacher_id"],\
              row["f_name"],row["l_name"],row["e_mail"],row["tel"]))