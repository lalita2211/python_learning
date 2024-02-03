# Program to check whether the given two strings are anagrams or not?
#both string have same character but in different order

    
s1 = "silent"
s2 = "listen"

if sorted(s1) == sorted(s2):
     print("given two string are anagrams")
else:
     print("given two string are not anagrams")
