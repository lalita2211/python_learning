#tuple is exactly same as list but tuple is immutable
# we can't modify the existing object in tuple
#we can't add or remove object from tuple
# tuple is only read only version of list
# we can use inedex and slice concept

t = (10,20,"harshit",10.5,10+20j)
print(type(t))
print(t)

print(t[0]) #index concept
print(t[1:4]) #slice operator

#if single value in tuple the it should end with comma

t = () #it is tuple datatype
print(type(t))
t = (2) #it is not tuple because it have single value without comma
print(type(t))
t = (10.5)
print(type(t))
t = (True)
print(type(t))
t = (10+20j)
print(type(t))

t = (10,)
print(type(t)) #it is tuple because it have comma with single value
