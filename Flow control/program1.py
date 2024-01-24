#Find smallest and biggest number using if else statement

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))

#find largest
if a>b and a>c:
    print("Largest number is:", a)
elif b>c:
    print("largest number is:", b)
else:
    print("Largest number is:", c)


#find smallest

if a<b and a<c:
    print("smallest number:", a)
elif b<c:
    print("smallest number is:", b)
else:
    print("smallest number is:", c)