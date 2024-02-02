#program to check wheter the given number is prime or not:

n = int(input("Enter a number"))

if n <= 1:
    print("this is not prime number")
else:
    a = 0
    for x in range(2,n+1):
        if n%x == 0:
            a = a+1
    else:
        if a == 1:
            print("{} is prime number".format(n))
        else:
            print("{} is not a prime number".format(n))

#another way
n = int(input("Enter a number"))
if n <= 1:
    print("this is not prime number")
else:
    is_prime = True
    for x in range(2,n):
        if n%x == 0:
           is_prime = False
           break
   
if is_prime == True:
    print("{} is prime number".format(n))
else:
    print("{} is not a prime number".format(n))


#shortcut of calculate prime number:
    """
    first we will calculate floor division of n number and caculte the prime for floor division
    """
n = int(input("Enter a number"))
if n <= 1:
    print("this is not prime number")
else:
    mid_value = n//2
    is_prime = True
    for x in range(2,mid_value):
        if mid_value %2 == 0:
            is_prime = False
            break
if is_prime == True:
    print("{} is prime number".format(n))
else:
    print("{} is not a prime number".format(n))
