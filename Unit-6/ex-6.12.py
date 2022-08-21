animals_dct = {1:"Cat", 2:"Dog", 3:"Tiger", 4:"Bird", 5:"Lion"}
sports_dct = {"1":"Football", "2":"Tennis", "3":"", "4":"Runnig"}
animals_dct.setdefault(6,"Rad")
print ("ค่า key ที่ 4 ใน animals_dct คือ", animals_dct.setdefault(4))
sports_dct.setdefault("5")
sports_dct.setdefault("6","Basketball")
animals_dct.setdefault(4, "Chicken")
print ("รายชื่อชนิดสัตว์ทั้งหมดใน animals_dct คือ", animals_dct)
print ("รายชื่อชนิดกีฬาทั้งหมดใน sports_dct คือ", sports_dct)