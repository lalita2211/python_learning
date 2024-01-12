str = "LalitaHarshit"

#get the range of character from below string
print(str[2:6]) #return subsctring is end by end-1 always and start from begin

#if we not defind begin then it will start from zero
print(str[ : 6])

#if we not defind end then it will take till end
print(str[6:])

#if we not define begin and end both then it reture entire string
print(str[:])

#in python we can define any range in slice operator,never going to get index error
print(str[3:1000])

#Slice operatore always going to move forward deirection
print(str[6:1]) #We will get empty string in this case