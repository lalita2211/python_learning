
#continue statement
#program : print shopping cart price and if price is >500 then print insurance required
cart = [200,300,600,400,800,540,900,150]
for i in cart:
    if i >= 600:
        print("insurance is required for price above 600")
        break #go to loop outside, next itration won't execute
    print(i)
print("outside of loop")

#continue statement
#program : print shopping cart price and if price is >500 then print insurance required

cart = [200,300,600,400,800,540,900,150]
for  i in cart:
    if(i>600):
        print("insurance is required for price above 600")
        continue #current itretion won't execute, the next will execute
    print(i)
print("outside of loop")

#program 2: - division to nummbers and if number is 0 then print error
list = [10,20,0,5,0,30]
for i in list:
    if i == 0:
        print("division is 0 will give infinity")
        continue
    print("division of {} is:".format(i), i/100 )

#break with nested loop
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i,j)

#continud with nested loop
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i,j)

