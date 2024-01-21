#nesting ternary operators
#program 1
#Take 2 imput number from keyword and 
# if both are equal then print both numbers are equal
#if 1st number min then print 1st min
#if 1st largest then print 1st largest


a = int(input("enter 1st value"))
b = int(input("Enter 2nd value"))

c = "both numbers are equal" if a == b else "First is smallest then 2nd number" if(a<b) else "1st number is grater then 2nd number"
print(c)

#program2
#take 3 number and find min value

a = int(input("enter 1st value"))
b = int(input("Enter 2nd value"))
c = int(input("enter 3rd value"))

min = a if a<b and a<c else b if b<c else c
print("minimum number is:", min)