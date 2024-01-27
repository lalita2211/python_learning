#to print inverted right angle tringle with * symbol
n = int(input("enter the number of row"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    n = n-1
    print()

#another way
n = int(input("enter the number of row"))
for i in range(n):
    print(("* ") * (n-i))
    
    