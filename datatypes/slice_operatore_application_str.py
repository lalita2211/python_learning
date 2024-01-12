s = "lalita"

#get the first and last character to uppercase using slice opeartor

print(s[0].upper() + s[1:len(s)-1] + s[-1].upper())

str1 = "lalita is a good developer"

#make the developer in captal letter
length = len(str1) #get the length of string
print("Length=", length)

a = str1[0:len(str1)-9] #get the string before developer
l = length-9 #get the length before developer
print(l)
b = str1[17:].upper() #make captial to developer
print("a=",a)
print("b=",b)
print(a + b)
