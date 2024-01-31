# WAP to convert first character, last character as uppercase and all remaining characters should be lowercase

s = input("enter a string")

print(s[0].upper()+ s[1:len(s)-1].lower() + s[-1].upper())