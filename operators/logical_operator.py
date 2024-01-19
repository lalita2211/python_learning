#logical operator

#for boolean type value

#and operator
#return true if both are true
print(True and True)

#return false if any one is false
print(False and True)
print(False and False)

#or operator
#return True if any one is true, return false if both false
print(True or True)
print(True or False)
print(False or False)

#not operator
#if value is true then return Fasle, if value is false then return True
print(not True)
print(not False)



#############################################################################


#For non boolean type value

#and operator
#result will always is non-boolean
#x and y => output will x/y

#if x evaultes true then output will y
#if x evaultes false then output will x

print (10 and 20) # output should 20
print(0 and 32) #output should be 0
print("lalita" and "harshit") #output will harshit
print('' and "lalita") #output will '' (empty)

#or operator
#result will always is non-boolean

#if x is true then output will x
#if x is false then output will y

print (10 or 20) # output should 10
print(0 or 32) #output should be 32
print("lalita" or "harshit") #output will lalita
print('' or "lalita") #output will lalita

#not operator
#result will always come in boolean
print(not "lalita") #false
print(not "") #True
print(not 0) #true
print(not []) #true


#############################################################################

#A program to check user name valid or not

user = input("enter your name:")
password = input("enter your password:")

if user == "lalita" and password == "lalita@123":
    print("user is valid")
else:
    print("user is not valid")
