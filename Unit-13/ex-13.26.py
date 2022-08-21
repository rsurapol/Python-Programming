import calendar
print("วันเริ่มต้นในสัปดาห์ =", calendar.firstweekday())
print("ปี 2017 มี 366 วัน =", calendar.isleap(2017))
print ("วันแรกและจำนวนวัน เดือนมกราคม ปี 2017 =", calendar.monthrange(2017, 1))
print("ปี 2017 เดือน 1 วันที่ 31 ตรงรหัสวัน =", calendar.weekday(2017, 1, 31))