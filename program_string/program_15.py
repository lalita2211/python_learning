#Find no of occurrences of each character present in given string with count( )
s = "lalita"
j = ""
for x in s:
    if x not in j:
        count = s.count(x)
        print("occurance of {} in string is {}".format(x,count))
    j = j+x

#another way
s = "lalita"
j = []
for x in s:
    if x not in j:
        j.append(x)

for ch in sorted(j):
    print("occurance of {} in string is {}".format(ch,s.count(ch)))
    
