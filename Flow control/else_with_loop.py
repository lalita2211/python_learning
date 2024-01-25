#else with loop
#if loop execute without break statement then else will execute only

for x in range(10):
    if x>=11:
        break
    print(x)
else:
    print("all value execute successfully")


for x in range(10):
    if x==5:
        continue
    print(x)
else:
    print("all value execute successfully")