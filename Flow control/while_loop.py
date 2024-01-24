# #print hello message ten time with while loop
# a = 1
# while a<=10:
#     print("hello")
#     a = a+1

# #print number from 1 to 10
# a = 1
# while a<=10:
#     print(a)
#     a = a+1

# # print the number from 1 to 20 which are divisible by 3
# a = 1
# while a<=20:
#     if a % 3 == 0:
#         print(a)
#     a = a+1

# #to display the sum of N number, n number take from keyborad

# n = int(input("Enter n number"))
# sum = 0
# x = 1
# while x<=n:
#     sum = sum+x
#     x = x+1
# print("sum of n number:", sum)

# #to display the sum of N number, n number take from keyborad using for loop

# n = int(input("enter n number"))  #5 1+2+3+4+5
# sum = 0
# x=1
# for i in range(x, n+1):
#     sum+=i
# print(sum)

# # print till name is equal to sunny
# n = ""
# while n != "lalita":
#     n = input("enter name of your fav")
# print("thanks for your confirmation")

# l = [0,1,2,4]
# for i in l:
#     m = i(i+1)/2
#     print(m)


l = [0,1,2,3,4,6]
length = len(l)
xor_all =0
for i in range(length+1):
    xor_all^=i
xor_arr =0 
for num in l:
    xor_arr ^=num

print(xor_all ^  xor_arr)


#nested loop

for i in range(3):
    for j in range(2):
        print("i={} and j={}".format(i,j))