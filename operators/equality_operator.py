#equality operator
#to check given values are equal or not

print(10==10)
print(23!=10)
print("lalita"=="lalita")
print(1==True)
print(10==10.0)

#it is comparision between int and string but return always False

print(10=="lalita")

#equality operator chaining
#if all the comparision reture true then output True otherwise False

print(10==3==43==54==10)
print(1==True==1)

#difference between is operator and == operator

#is operator means for reference or address comparision
#if object will same then reture True

# == operator means for content comparision
#if content same and object not then return True

l1 = [10,20,30]
l2 = [10,20,30]
print(id(l1))
print(id(l2)) #id is different for both

print(l1 is l2) #return false bcz address different
print(l1 == l2) #return true bcz content same

l3 = l1
print(id(l3)) #l3 address is same with l1
print(l3 is l1)
print(l3 == l1)
