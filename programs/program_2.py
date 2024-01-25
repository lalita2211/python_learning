#genrate prime number which are less then or equal to given number


n = int(input("enter a number"))

n1 = 2
while n1<=n:
    is_prime = True
    for x in range(2,n1):
        if n1 % x == 0:
            is_prime = False
            break
    if is_prime == True:
        print(n1)
    n1 = n1+1