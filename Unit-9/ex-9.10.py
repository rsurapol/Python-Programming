class LessthanStockError(Exception):
    def __init__(self):
        Exception.__init__(self, "สินค้าคงเหลือน้อยกว่าที่กำหนดไว้")

x = 10
n = int(input("ขายสินค้าได้ = "))
z = x - n
if z < 5:
    raise LessthanStockError
else:
    print ("สินค้าคงเหลือ =", z, "ชื้น")