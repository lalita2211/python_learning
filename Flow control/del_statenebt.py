#del statememnt
"""
del is a keyword in python
we can use it for delete the variable
Advantage: improve free memory
"""

#del with immutable object
s = "lalita"
del s
print(s) #success

#we can delete entire string but can't delete the element of string
s1 = "harshit"
del s1[0]
print(s1) #error

#del with non
#if we delete variable and then assign none then that will available but object eligible for garbage
x = 10
del x
x = None
print(x)

#del with multiple value
#if we delete all reference variable then only reference object will eligible for garbage 
s = "lalita"
s1 = s
s2 = s1
del s
# print(s) : error
print(s1)
print(s2)