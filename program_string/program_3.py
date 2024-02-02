#Write a Program To REVERSE content of the given String by using while loop
s = input("Enter a string")
length = len(s)-1
while length >= 0:
    print(s[length],end="")
    length = length-1