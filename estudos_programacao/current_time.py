import time

t = time.localtime(time.time())
localtime = time.asctime(t)
stri = "Current Time: " + localtime

print(stri)
