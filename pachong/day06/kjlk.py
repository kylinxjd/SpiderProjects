import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

print(localtime.tm_mday)

print(time.asctime())
