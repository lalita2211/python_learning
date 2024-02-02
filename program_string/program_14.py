# Program to remove duplicate characters from the given input String

s = "AZZBCCDRREHHFJJYTTT"
s1 = s[0]
output = s1
for x in s:
   if x != s1:
      s1 =  x
      output = output + s1
print(output)

#another way

s = "AZZBCCDRREHHFJJYTTT"
output = ""
for ch in s:
   if ch not in output:
      output = output + ch
print(output)

# using set()
s = "AZZBCCDRREHHFJJYTTT"
s1 = set(s) # not getting in order
print(''.join(s1))