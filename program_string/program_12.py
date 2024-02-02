#Program for the requirement,input aaaabbbccz and expected output 4a3b2c1z

s = "aaaabbbcczzzttt"
s1 = ""

p_chr = s[0]
c = 0
a = 0
for x in s:
    if x == p_chr:
        c = c+1
        
    else:
        s1 = s1 + str(c) + p_chr
        p_chr = x
        c = 1
    
    if a == len(s)-1:
        s1 = s1 + str(c) + p_chr
    a = a+1

print(s1)