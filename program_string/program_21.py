#  Program to check whether the given string is palindrome or not?
s = input("enter a string")
s1 = s[: : -1]
if s == s1:
    print("string is palindrome")
else:
    print("string is not palindrome")