a = "20+5j"; b = "15+6j";
x = complex(a)
y = complex(b)
z = complex(7,5)
print ("ผลลัพธ์การแปลงชนิดข้อมูลจำนวนเชิงซ้อนจากตัวแปร a =", x)
print ("ผลลัพธ์การแปลงชนิดข้อมูลจำนวนเชิงซ้อนจากตัวแปร b =", y)
print ("ค่าจำนวนจริงของ c =", x.real, "และค่าจินตภาพของ c = ", x.imag)
print ("ผลลัพธ์การแปลงเครื่องหมายตัวดำเนินการของตัวแปร y =", y.conjugate())
print ("ผลลัพธ์การสร้างคู่อันดับจากตัวแปร z =", z)