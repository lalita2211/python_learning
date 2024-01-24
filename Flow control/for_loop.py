
#for loop
#find one by one character with index value
s = "lalita Agarwal"
a = 0
for x in s:
    print("the charactter present at {} index: {}".format(a,x))
    a = a+1

#got value from keyword and find one by one character with index value
    
s = input("enter the name")
a = 0
for x in s:
    print("charcter present at {} index: {}".format(a,x))
    a= a+1

#print statement for 10 time

s = "Hello welcome to python for loop"

for x in range(10):
    print(s)

#print numbers from 1 to 10

r = range(1,11)
for x in r:
    print(x)

#display odd number from 0-20
    
r = range(0,21)
for x in r:
    if x % 2 != 0:
        print("odd numbere is:",x)

#print number from 10 to 1
r = range(10,0,-1)
for x in r:
    print(x)

    
#to print the sum of number of the given list

l = eval(input("enter numbers as list"))
sum = 0
for x in l:
    sum = sum+x
print(sum)

# we can use sum function also:  print("sum=", sum(l))