#REPRESENT A GROUP OF BYTE VALUE
# value should be within range 0-255
#defind by byte() function
#it is immutable, we can't change existing object

l = [10,20,30,40]
b = bytes(l)
print(type(b))
print(b)
for x in b:
    print(x)

print(b[1]) #index and slice operators are applicable



#bytearray
#bytes and bytearray are same except bytearray is mutable, we can change exisiting value
#create by bytearray() function
#range should be within 0-255

l = [10,20,30,40]
ba = bytearray(l)
print(type(ba))
print(ba)
for x in ba:
    print(x)
    ba[1] = 22 #we can change exisiting value
    for x in ba:
        print(x)