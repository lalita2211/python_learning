# Write a Program To REVERSE internal content of each word

s = "lalita will be a good developer"
l = s.split()
for x in l:
    print(x[: : -1],end=" ")