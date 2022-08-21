class PassTestError(Exception):
    pass
class FailTestError(Exception):
    pass

try:
    n = int(input("กรุณากรอกคะแนน : "))
    if n < 50:
        raise FailTestError
    else:
        raise PassTestError
except FailTestError:
    print ("คุณไม่ผ่านเกณฑ์ 50 คะแนน คุณที่คุณได้ %d คะแนน" %n)
except PassTestError:
    print ("ยินดีด้วยครับคุณสอบผ่าน คะแนนที่คุณได้ คือ %d" %n)
except ValueError:
    print ("คุณป้อนข้อมูลไม่ถูกต้อง")