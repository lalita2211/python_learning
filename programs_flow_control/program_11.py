#to print inverted pyramind pattten witn * symbol

n = int(input("enter the number of row"))

for i in range(n):
    print(" "*i, "* "*(n-i))
    