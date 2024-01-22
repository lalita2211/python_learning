#reader three float value from keyword with comma sepration and print sum


a,b,c = [float(x) for x in input("Enter three values").split(',')]
print("sum of three values=", a+b+c)


