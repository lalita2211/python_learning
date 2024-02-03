# Program for the requirement,input: ABAABBCA and expected output: A4B3C1
s = "ABAABBCA"
d = {}
output = ""
for ch in s:
    d[ch] = d.get(ch,0)+1
for k,v in sorted(d.items()):
    output = output + k + str(v)
print(output)