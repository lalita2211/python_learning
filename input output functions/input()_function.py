
#Take 2 number and print sum
a = int(input("enter 1st value"))
b = int(input("enter 2nd value"))
sum = a+b;
print("sum is:", sum)

print("the sum is:", int(input("enter 1st value")) + int(input("enter 2nd value")))

#take employee details and print

name = input("enter the name")
e_number = int(input("enter number"))
salary = float(input("enter salary"))
address = input("enter address")
married = bool(input("Empolyee married ? [True/False]:"))

print("Employee Number: \t", e_number)
print("Employee Name: \t", name)
print("Employee Salary: \t", salary)
print("Employee Address: \t", address)
print("Employee Mariage status: \t", married)

#bool() function provide value false if string is empty only otherwise always return true
# if we wnt result is boolean value then use always eval() function

marriage_status = eval(input("married or not ? [True/false]"))
print("marriage status=",marriage_status )
