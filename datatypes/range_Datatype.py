# a sequence of number

#range datatype defind by range() function

r = range(10)
print(r)

for x in r:
    print(x)

#form1:
#pass only 1 argument:
r = range(13) #value will b (0-12) 
print(r)
for x in r:
    print(x)

#form2:
#pass 2 argument
    #1st is begin and 2nd is end
r = range(5,15) #value will end-1
print(r)
for x in r:
    print(x)

#form3:
#pass 3 argument
#1st is begin and 2nd is end and 3rd is inc/dec
r = range(2,21,2)
print(r)
for x in r:
    print(x)

#pass decrement
    #if we pass negative value then begin must be bigger then end value
r = range(21,2,-2)
print("range=",r)
for x in r:
    print("x=",x)