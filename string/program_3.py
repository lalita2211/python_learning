# WAP to check whether provided username and passwords are valid or not. Username is not case sensitive, but password should be case sensitive.

user = input("enter username").title() #Lalita22
password = input("enter password") #Lalita@22

if user == 'Lalita22' and password == 'Lalita@22':
    print("User name and password are valid")
elif user != 'Lalita22' and password != 'Lalita@22':
    print("user name and password are not valid")
elif password != 'Lalita@22':
    print("password is not valid")
elif user != 'Lalita22':
    print("user name is not valid")


    