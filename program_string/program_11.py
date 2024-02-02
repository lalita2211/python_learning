##Program for the requirement,input a3z2b4 and expected output aaabbbbzz

s = "a3z2b4"
s1 = ""
for x in s:
    if x.isalpha():
        ch = x
    else:
        d = int(x)
        s1 = s1 + ch*d
print(''.join(sorted(s1)))