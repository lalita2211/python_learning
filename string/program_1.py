# to find index of all occurrence of given substring

# s = "lalita agarwal"
# i = s.find('a')
# print(i)
# i = s.find('a',2,)
# print(i)
# i = s.find('a',6,)
# print(i)
# i = s.find('a',8,)
# print(i)
# i = s.find('a',10,)
# print(i)


#dynamicaly

s = "lalita agarwal"
sub = "a"
i = s.find(sub)

if i == -1:
    print("sunstring is not found")
else:
    count = 0
    while i != -1:
        count = count+1
        print("{} sunscrint at index {}".format(sub,i))
        i = s.find("a",i+1,)
        
    print("count=",count)
        



