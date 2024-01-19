#bitwise operatpr
#bitwise operator works with only int and bool value

#& and operator
#if both values are true then return true
print(0 & 0) #output will be int value
print(0 & 1)
print(1 & 1)
print(10<11 & 11==11) 
print("bitwise and with int value:", 4&5)  #first it will convert 4 and 5 to binary then calculate & operator bit by bit


########################################################################


#| or operator
#if any one value is true then return true
print(0 | 0) #output will be int value
print(0 | 1)
print(1 | 1)
print("bitwise or with int value:", 4|5)  #first it will convert 4 and 5 to binary then calculate | operator bit by bit


########################################################################


#^ operator
#if both values are different then retrun true
print(0 ^ 0) #output will be int value
print(0 ^ 1)
print(1 ^ 1)
print("bitwise x-or with int value:", 4^5)  #first it will convert 4 and 5 to binary then calculate ^ operator bit by bit


########################################################################


#bitwise ~ component operator

"""
~ bitwise means 0 will become 1 and 1 will become 0
* The most significate bit (MSB) acts as sign bit
* 0 -> positive number
* 1 -> Negative number
positive number will represent directly to memory
negative number represent memory by 2's form
1's form is: convert 0 to 1 and 1 to 0
2's form is: add 1 to 1's form result
"""
print(~4)
print(~5)
print(~-4)

########################################################################

#bitwise Left shift (<<) operator
"""
Move bits to left side based on given number.
left side bits will be gone and vacant cell will be add to right side
These vacent cell always filled with zero
"""
print(10<<2)

########################################################################

#bitwise Left shift (<<) operator
"""
Move bits to right side based on given number.
right side bits will be gone and vacant cell will be add to left side
These vacent cell is significate bits but not filled with zero
"""
print(10>>2)

########################################################################

#bitwise operator with boolean value

print(True & False)
print(False | False)
print(True ^ False)
print(~True)
print(~1)
print(True<<2)
print(True>>2)