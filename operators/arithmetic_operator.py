#in python total 7 arithmetic operator

# 1. plus (+) operator
a = 10
b = 20
print(a+b) #plus with int value

#if we operate + operator with string then both value should be string

print("lalita"+"harshit")

#if we don't have string value then we can convert to string via using str() method

print("lalita" + str(12))

###############################################################


# 2. minus(-) operator
print(a-b)

###############################################################

# 3. multiplicaion(-) operator
print(a*b)

#if we operate * operator with string then one value should be string and another should be int only
#string value should be only one and int can be more then one
#order of argument doesn't matter

print("lalita" * 2)
print(2*"lalita")

#if we don't have int value then we can convert via int() method

print("harshit" * int('2'))

###############################################################

# 4. Exponetial/power (**) operator

#if is power operator
print(10**2) #it means 10*10

###############################################################

# 5. modular (%) operator
print(10%3)

###############################################################

# 6. Division(/) operator
#in python 3.0 division operator always give value in floating point 
print(10/2) #result will be always in floating point


###############################################################

# 7. Floor Division (//) operator
#it give value in integral and floating point both based on argument
#if both arguments are int then result will be in integral 
#if at least one argument is float then result will be in floating point
# it is take the floor value, means the nearest value of float value

print(10//2) #result will be int type value
print(10.2//2) #result will be floating value
print(10//3) #result will be int type and will take floor value
print(10.0//3) #result will be float type but first take floor value then put floating poing



