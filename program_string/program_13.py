# Program for the requirement,input a4k3b2 and expected output aeknbd

s = "a4k3b2"
s1 = "abcdefghijklmnopqrstuvwxyz"
output = ""
a = 0
while a < len(s):
   if s[a].isalpha():
       #print(s[a])
       output = output + s[a]
       ch = s[a]
   else:
       j = s1.index(ch)
       #print(s1[j + int(s[a])])
       output = output + s1[j + int(s[a])]
   a = a+1
print(output)

#another way

s = "s4t2k7"
output = ""
for x in s:
    if x.isalpha():
      output = output + x
      unicode = ord(x)
    else: 
       j = unicode + int(x)
       output = output + chr(j)
print(output)