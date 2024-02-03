#To generate words from given input strings by taking characters alternatively
s = "lalita"
s1 = "agarwal"
i = 0
j = 0
s3 = ""

while i < len(s) or j < len(s1):
    if i < len(s):
        s3 = s3 + s[i]
    if j < len(s1):
        s3 = s3 + s1[j]
    i = i+1
    j = j+1
print(s3)
