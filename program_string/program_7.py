# Program:Print characters present at even & odd index separately for given string

s = "abcdefghijkl"
a = 0
while a < len(s):
    if a % 2 == 0:
        print("{} character at even index{}".format(s[a],a))
    else:
        print("{} character at odd index{}".format(s[a],a))
    a = a+1


#another way

s = "abcdefghijkl"
a = 0
while a < len(s):
    print("charcter at even:", s[a])
    a = a+2
a = 1
while a < len(s):
    print("charcter at odd:",s[a])
    a = a+2

#another way
    
s = "abcdefghijkl"
print("charcter at even=",s[0 : : 2])
print("charcter at odd=",s[1 : : 2])