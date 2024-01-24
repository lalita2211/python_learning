#check given number is in between 1 and 100 or not

a = int(input("enter a number"))

if a >=1 and a<=100:
    print("the number {} is between 1 and 100".format(a))
else:
    print("the number is not between 1 and 100")