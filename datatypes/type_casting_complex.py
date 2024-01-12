#int to complex
#form1
#if we pass only 1 argument then that numner will be real number
print(complex(10))
print(complex(0b0011))
#form2
#if we pass 2 argument the one will real and second will imaginary number
print(complex(10,20))
print(complex(0b0011,12))
print(complex(3,0b0011))



#float to complex
#form1
print(complex(10.5))
#form2
print(complex(10.5,5.5))



#bool to complex
#form1
print(complex(True))
#form2
print(complex(True,False))


#string to complex
#form1
#String should be contain int or float value with basse 10
print(complex("10"))
print(complex("10.9"))

#form2
#if 1st argument is string then we can't pass 2nd argument as a string
#secong argument should not be string
#so basically String to complex convert is not possible with form 2
