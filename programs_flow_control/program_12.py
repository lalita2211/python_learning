#print diamond pattern with * symbol
n = int(input("enter the number of row"))
for i in range(n):
    print(" "*(n-(i+1)) + "* "*(i+1))
for j in range(n-1):
    print(" "*(j+1) + "* "*(n-(j+1)))