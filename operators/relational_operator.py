#comparision between numbers
a= 10
b = 20
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)

#compariosion between string
#comparision between unicode of character

#find unicode of character, use ord() function
print("unicode of a:", ord('a')) #return unicode of a

#find character of unicode, use char() function
print("character of 97:", chr(97)) #returen character of 97

s1 = a
s2 = b

print(s1>s2) #it will check unicode
print(s1>=s2)
print(s1<s2)
print(s1<=s2)

s1 = "lalita"
s2 = "harshit"

print(s1>s2) #it will check unicode of only first character
print(s1>=s2)
print(s1<s2)
print(s1<=s2)

s1 = "Lalita"
s2 = "lalita"

print(s1>s2) #it will check unicode of only first charcter
print(s1>=s2)
print(s1<s2)
print(s1<=s2)

# with bool type
print(True>False)
print(False>True)
print(1>False)
print(23<True)

#Relational operator chaining
#comparision with multiple value

#if all the comparision reture true then output will be True
#if any one comparision reture false then output will be False
print(10>20>30>40)
print(10>29>20)
print(10<20<30>11)

