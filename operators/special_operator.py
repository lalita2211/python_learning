#Identitly operators

#is : if both argumenet pointing to same address return true
#is not: if both argumenet pointing to not same address return true

a = 10
b = 10
print(id(a))
print(id(b))
print(a is b)
print (a is not b)
l = [10,20,30]
l1 = l
print(id(l))
print(id(l1))
print(l is l1)
l3 = [10,20,30]
print(id(l3))
print(l is l3)

#Membershit operators

#in = if the value is member then return true
#not in = if the value is not member then return true
#it is case senstetive

a = "I am learning python"
print("am" in a)
print("Am" in a)
print("i" not in a)
print("" in a)
print("lal" not in a)

#operator precedence
a= 30
b=20
c=10
d=5
print((a+b) * c/d)

