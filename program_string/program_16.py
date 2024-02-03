#No of occurrences of each character present in given string without count()
#using dictionary

s = "lalita"
d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1

for k,v in sorted(d.items()): #getting key value seperately
    print("{} character appears in string {}".format(k,v))