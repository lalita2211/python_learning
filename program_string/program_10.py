# Program for the requirement,input a4b3c2 and expected output aaaabbbcc

s = "a4b3c2"
s1 = ""
i = 0
while i<len(s):
     s1 = s1 + s[i] * int(s[i+1])
     i = i+2
print(s1)

#another way

s = "a4b3c2"
s1 = ""
for x in s:
     if x.isalpha():
          ch = x
     else:
          d = x
          s1 = s1 + ch * int(d)
print(s1)




