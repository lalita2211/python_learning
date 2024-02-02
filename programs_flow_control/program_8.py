#to print ringh angle tringle pattern with * symbol

n = int(input("enter the number of row"))
for i in range(1,n+1):
    print(("*" + " ") * i )


#another way
n = int(input("enter the number of row"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()