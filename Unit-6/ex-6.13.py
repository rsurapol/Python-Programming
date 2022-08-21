animals_dct = {1:"Cat", 2:"Dog", 3:"Tiger", 4:"Bird", 5:"Lion"}
sports_dct = {"1":"Football", "2":"Tennis", "3":"", "4":"Runnig"}
animals_dct1 = {6:"Cow", 7:"Rad"}
sports_dct1 = {"3" :"Basketball"}
animals_dct.update(animals_dct1)
sports_dct.update(sports_dct1)
print (animals_dct)
print (sports_dct)
sports_dct.update({"5":"Table tennis"})
sports_dct.update({"2":"Racing"})
print (sports_dct)