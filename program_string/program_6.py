#Program To REVERSE internal content of every 2nd word present in given string

s = "lalita will be a good developer"
l = s.split()
l1 = [ ]
i = len(l)
a = 0
while a < i:
    if a % 2 != 0 :
      l1.append(l[a][ : : -1])
    else:
       l1.append(l[a])
    a = a+1
print(' '.join(l1))


    