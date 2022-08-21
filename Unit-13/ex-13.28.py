import time
print(time.asctime())
print(time.asctime(time.gmtime()))
print(time.asctime(time.localtime()))
print(time.strftime("5a %d %b %Y %H:%M:%S"))
print(time.strftime("5a %d %b %Y %H:%M:%S", time.gmtime()))