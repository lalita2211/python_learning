# Program to find the number of occurrences of each vowel present in given string

s = "dUrgasoftwaredurga"
vowel = ['a','e','i','o','u','A','E','I','O',"U"]
d = {}
for ch in s:
    if ch in vowel:
        d[ch] = d.get(ch,0)+1
for k,v in sorted(d.items()):
    print("{} vowel character appear in string {}".format(k,v))



    
       

