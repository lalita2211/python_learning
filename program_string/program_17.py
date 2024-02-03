# Program for the requirement,input: ABAABBCA and expected output: 4A3B1C

s = "ABAABBCA"
d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1


for k,v in sorted(d.items()):
    print(v,end="")
    print(k,end="")
