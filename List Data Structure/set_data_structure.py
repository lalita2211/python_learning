# program 1: WAP to eliminate duplicate present in list
l = [10,20,10,40,30,20,50,30,40]
l2 = sorted(set(l))
print(l2)

#without set
l = [10,20,10,40,30,20,50,30,40]
l1 = []
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)

#program 2: WAP to print different vowel present in given word

s = "lalita agarwal"
vowel = "aeiou"
s1 = { x for x in s if x in vowel }
print(s1)

#use intersection
s = "lalita agarwal"
vowel = {'a','e','i','o','u'}
s1 = set(s)
s2 = s1.intersection(vowel)
print(s2)
print(s1&vowel)
