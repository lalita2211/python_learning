#to print square pattern of * symbol

n = int(input("enter a number"))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print("\n")
        
#another way

n = int(input("enter a number"))
for i in range(n):
    print("*" * n)
