class car:
    brand = "Toyota"
    vehecle = "Yaris"
print (getattr(car, "brand"))
print (getattr(car, "color", "Not Found"))
print (getattr(car, "vehecle", "Not Found"))