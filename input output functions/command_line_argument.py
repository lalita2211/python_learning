#command line argument

"""
 1. The argument which are passing by command promt are called command line argument

 2. We can read these argument by:
    sys module
    sys module have argv variable

 3. argv is use for read the argumnt

 4. argv is list type

 4. command line argument's values are always consider as string

 5. argument is seprated by space

 6. We can pass argument as string within double quote only. that string will consider 1 argument only

 7. Advantage of CMD: we can customize behaviour of application based on requirement

 8. if we try to access cmd argument with the out of range then will get index error

 9. 1st argument of cmd is always file name
"""

#Program 1
#to print information of command line arguments:

from sys import argv



#program 2
    #sum of given arguments
x1 = argv[1:]
sum = 0
for s in x1:
    sum = sum+ s
    
print("sum=", sum)
