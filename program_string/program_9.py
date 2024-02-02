# Program:Sort characters of the string, first alphabet symbols followed by digits

s = "B4A1D3"


if s.isalnum():
   albhabet = ""
   digit = ""
   
   for x in s:
      if x.isalpha():
         albhabet = albhabet + x
      if x.isdigit():
         digit = digit + x
   print("albhabet = ",albhabet)
   print("digit = ",digit)
   l = sorted(albhabet) + sorted(digit)
   print(''.join(l))
  
