#Order is not important in set
#duplicate values are not allowed
#represent within {}

s = {10,20,30,40}
print(type(s))
print(s)

s = {10,20,30,20,10} #duplicate value will be ignored
print(s)
print("address of s:", id(s)) 


s.add(60) #we can add value to existing object by use add() method only
print(s) 
print("address of s:", id(s)) #address will be same as set is mutable

s.remove(20) #we can remove value 
print(s)
print("address of s:", id(s)) #address will be same as set is mutable

s = {10,"lalita",1.5,2+6j+True} #htreogeneous object are allowed
print(type(s))
print(s)
print("address of s:", id(s)) 

#if we assign empty value to variable then that variable will be dict type as dict is also represent within {} and python give prefer to dict 

s= {}
print(type(s)) #tyoe of s should be dict
print(s)


#if we want to assign empty value to set datatype then we have to use set()
s = set()
print(type(s)) #tyoe of s should be set
print(s)
print("address of s:", id(s))

s = {10,20}
print("address of s:", id(s))

s = {30,40}
print("address of s:", id(s))


#frozenset
#same as set except it is immutable
#to define frozenset we have to use frozenset() function

l = [20,30,43,20]
fs = frozenset(l)
print(fs)
print(type(fs))

s = {23,34,53}
fs = frozenset(s)
print(fs)
print(type(fs))


