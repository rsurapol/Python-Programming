animals_dct = {1:"Cat", 2:"Dog", 3:"Tiger", 4:["Bird","Chicken"], 5:"Lion"}
animals_dct1 = animals_dct.copy()
print ("animals_dct =", animals_dct)
print ("animals_dct1 =", animals_dct1)
animals_dct[5] = "Rad"
animals_dct[4].remove("Bird")
print("---------- ปรับปรุงข้อมูลครั้งที่ 1 ----------------")
print ("animals_dct =", animals_dct)
print ("animals_dct1 =", animals_dct1)
print("---------- ปรับปรุงข้อมูลครั้งที่ 2 ----------------")
animals_dct1[5] = "Snake"
animals_dct1[4].remove("Chicken")
print ("animals_dct =", animals_dct)
print ("animals_dct1 =", animals_dct1)