# Creation of list with square value from 1 to 10

l = []

for x in range(1,11):
    l.append(x*x)
print(l)

l = [x*x for x in range(1,11)]
print(l)

#########################################################################################


# get power of 2 of 1 to 5 number
l = []
l = [ 2**x for x in range(1,6)]
print(l)


#########################################################################################


#Create a list to 1 - 200 which are divisible by 10

l=[]

l = [i for i in range(1,201) if i%10 == 0]
print(l)

#########################################################################################


# Create a list with element those present in l1 but not in l2

l1 = [10,20,30,40]
l2 = [30,40,50,60]

l3 = [x for x in l1 if x not in l2]
print(l3)

#########################################################################################


# Create a list with element those present in both l1 and l2
l1 = [10,20,30,40]
l2 = [30,40,50,60]

l3 = [x for x in l1 if x in l2]
print(l3)


#########################################################################################


#create a new list object only with the first letters as elements.

l = ["lalilta", "harshit", "kavish", "honey"]
l1 = [ x[0] for x in l]
print(l1)


#########################################################################################



# Program to convert the string to list and then create nested list with length of each work
s = "the quick brown fox jumps over the lazy dog"
l = s.split()

l1 = [[x.upper(),len(x)] for x in l]
print(l1)


#########################################################################################



# Program to display unique vowel present in given word

s = 'aeoeiaouie' 
vowel = ['a','i','o','e','u']
l=[]
for x in s:
    if x in vowel:
        if x not in l:
            l.append(x)
print(sorted(l))

#########################################################################################

#using list comprehension

s = 'aeoeiaouie' 
vowel = ['a','i','o','e','u']

l = [x for x in vowel if x in s ]
print(l)