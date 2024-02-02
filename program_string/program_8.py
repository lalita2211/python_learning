# Program to merge characters of 2 strings by taking characters alternatively
#if both string have same length
s1 = "lalita"
s2 = "lavina"

i = 0
j = 0
s3 = ""
while i < len(s1) or j < len(s2):
    s3 = s3 + s1[i] + s2[j]
    i = i+1
    j = j+1
print(s3)


#if both dont have same length

s1 = "lalita"
s2 = "harshit"

i = 0
j = 0
s3 = ""
while i<len(s1) or j<len(s2):
    if i < len(s1):
        s3 = s3 + s1[i]
    if j < len(s2):
        s3 = s3 + s2[j]
    i = i+1
    j = j+1
print(s3)