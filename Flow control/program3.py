#take a single digit number from the keyword and print its value in english word

n = int(input("enter any number from 0-9"))
if n == 0:
    print("zero")
elif n == 1:
    print("one")
elif n == 2:
    print("two")
elif n == 3:
    print("three")
elif n == 4:
    print("four")
elif n == 5:
    print("five")
elif n == 6:
    print("six")
elif n == 7:
    print("seven")
elif n == 8:
    print("eight")
elif n == 9:
    print("nine")
else:
    print("please enter number in 0-9 only")


#another way
    
list = ["zero","one","two","three","four","five","six","seven","eight","nine"]
n = int(input("enter any number from 0-9:"))
print(list[n])