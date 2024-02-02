#Write a Program To REVERSE order of words present in the given string
s = input("enter a string")
l = s.split()
l1 = l[ : :-1]
print(" ".join(l1))

#another way

s = input("enter a string")
l = s.split()
l1 = l[ : :-1]
for x in l1:
    print(x,end=" ")


#another way
    
s = input("enter a string")
l = s.split()   
i = len(l)-1
while i>=0:
    print(l[i], end=" ")
    i = i-1