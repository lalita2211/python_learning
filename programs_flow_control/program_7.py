# to print square pattern with albhabet symbol
n = int(input("enter the number of row"))
a = ord('A')
for i in range(n):
    for j in range(n):
        print(chr(a), end=" ")
    a = a+1
    print("\n")

#another way
    
n = int(input("enter the number of row"))
for i in range(n):
    print((chr(65+i)+" ")*n)
    
    