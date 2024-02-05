#print object of list with +v index nd -ve index
l = [10,20,30,40,50,60,70,80]
a = 0
while a < len(l):
    print("{} object appear at {} positive index and {} nagative index".format(l[a],a,a-len(l)))
    a = a + 1

##############################################################################################################

# Program to append 1 - 100 number to list which devided by 10
l = []
r = range(1,101)
for x in range(1,101):
    if x % 10 == 0:
         l.append(x)
print(l)

##############################################################################################################

# Program to remove all occurance:

l = [10,20,10,30,10,45,34,10]
n = int(input("enter the number to remove from list"))
if n in l:
    for x in l:
        if x == n:
            l.remove(x)
    print(l)
else:
    print("element is not exist")

##############################################################################################################
    
# cloning concept

l = [10,20,30]
l1 = l
print(id(l),"\n value of ll:",l)
print(id(l1),"\n value of ll:",l1)
l1[2]=40
print(id(l),"\n value of ll:",l)
print(id(l1),"\n value of ll:",l1)

l = [10,20,30]
l1 = l[ : ]
print(id(l),"\n value of ll:",l)
print(id(l1),"\n value of ll:",l1)
l1[2]=40
print(id(l),"\n value of ll:",l)
print(id(l1),"\n value of ll:",l1)


###############################################################################################################

#Nested list

l = [[10,20,30],[40,50,60],[70,80,90]]

for x in l:
    for y in x:
        print(y,end=" ")
    print()
    