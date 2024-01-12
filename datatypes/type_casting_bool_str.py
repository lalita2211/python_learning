#convert to bool

#int to bool
#If the argument is 0 then it will consider False other then True only
print(bool(10))
print(bool(0b00111))
print(bool(0b0000))
print(bool(000))

#float to bool
print(bool(10.5))
print(bool(0.000))
print(bool(0.0001))

#complex to bool
print(bool(0+0j))
print(bool(0+1j))
print(bool(0b0011+0j))

#string to bool
#if the string is empty then it will consider False other then True only
print(bool(""))
print(bool("True"))
print(bool("False"))
print(bool("yes"))


#Convert to String
#We can easily convert any number to string without any rule

#int to str
print(str(3))
print(str(0b0011))

#float to str
print(str(10.5))

#bool to str
print(str(True))

#complex to str
print(str(10+2j))