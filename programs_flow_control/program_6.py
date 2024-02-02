#to print square pattern with provided fixed digit in every row

n = int(input("enter the number of row"))

for i in range(1,n+1):
    for j in range(n):
        print(i,end=" ")
    print(" \n")