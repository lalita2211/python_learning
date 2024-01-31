#WAP to check type of charcher enterned from the keyword

s = input("Enter a string")

if s.isalnum():
    print("All charchers are alpha numbers")
elif s.isalpha():
    print("All charchters are alphabatics")
elif s.isdigit():
    print("All charchter are numeric")
elif s.islower():
    print("All charters are in lowercase")
elif s.isupper():
    print("All charters are in uppercase")
elif s.istitle():
    print("string is in title case")
elif s.isspace():
    print("string containg only space")
else:
    print("string type is not consider")