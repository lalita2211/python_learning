#Mutable example

x= 10
y = x #now y will consume x memory

print("x=",x)
print("y=",y)
print("memory of x:", id(x))
print("memory of y:", id(y)) #both memory location should be same

y = y+1 #now y will consume new memory

print("y=",y)
print("memory of Y:", id(y))

#Immutable example

a = 20
print("a=", a)
print("memory of a:", id(a))

a = a+1 #now a will consume new memory
print("a=", a)
print("memory of a:", id(a))