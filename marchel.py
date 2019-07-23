import platform
a = 0 
for i in range(9999):
    a += i
print("finish job , result=%i" % a )
print("this is " , platform.system())