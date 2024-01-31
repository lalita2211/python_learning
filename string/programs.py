# # 1. display character of given sttring  index wise(positive and nagative)

# s = input("enter a string")
# for i in s:
#     print(i,end="")
# print()

# a = 1
# for i in s:
#     print(s[-a],end="")
#     a = a+1

# a = 0
# for i in s:
#     print("\n the character at +ve index : {} and the charcter ar -ve index : {} is : {}".format(a,a-(len(s)),i))
#     a = a+1

# ########################################################################
    
# # 2. remove space from string

# s = input("enter a string").strip()
# if s == "lalita":
#     print("she is lalita")
# else:
#     print("she is not lalita")

# #######################################################################
    
# #3. find index value

# #find() #left to right
# s = input("enter a string")
# print(s.find("a"))

# #rfind() : right to left
# print(s.rfind("a"))

# #particular boundary
# print(s.find("a",2,7))


# #index()

# #program to find the index of @ in mail id

# s = input("enter your mail id")
# print(s.index("@"))

# #rindex()
# print(s.rindex("@"))

# ########################################################################

# # 4. Replace a string with another

# s = "lalita and harshit"
# print(s.replace("lalita", "lavi"))

# #program to find count of space of string without count() function

# s1 = s.replace(" ","")
# print("the count of spaces", len(s)-len(s1))


########################################################################

# 5. Spliting of string

# s = "lalita will be good developer"
# l = s.split()
# for x in l:
#     print(x)

# date = "22-03-1996"
# l = date.split("-")
# for x in l:
#     print(x)

# ########################################################################
    
# # 6. joining of string
# l = ["lalita", "is", "a", "good", "developer"]
# s = "-".join(l)
# print(s)

# ########################################################################