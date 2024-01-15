l = [10,20,"lalita",45,"harshit",66,10.4,10+20j]
print(l)
print(type(l))

#order is important for the list
#value should be represent within square bracket
#Heterogeneious object are allowed
#duplicate object can be assign

l1 = [10,20,10,30,40]
print(l1)
print(type(l1))

#we can add or remove object by append and remove method
l.append(777)
print(l)
l.remove(10.4)
print(l)

#As list is order preserved we can use index concept and slice operator
print(l[4])
print(l[3:6])
print(l[-2])

#list is mutable, we can change the exising object
l[3] = 48
print(l)
