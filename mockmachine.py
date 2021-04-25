import random
n = random.randrange(1234567890)




print("welcome to bank of lafiagi ")
print("Do you have account with us:1(yes)2(no)")
selectedoption =int(input(""))

if(selectedoption==1):
    login=(input("Your email\n"))
    login(input("password\n"))
    print("welcome")

if(selectedoption==2):
    print("****Register****")



    first_name=(input("what is your Firstname?\n"))
    last_name=(input("what is your lastname?\n"))
    email=(input("what is your email address?\n"))
    password=(input("please creat strong password\n"))
    password=len(password)
    
    

    
print("Your first name is:",first_name)
print("your last name is:",last_name)
print("your email address is:",email)
print("your password is:",'*'*password)
print("your account number is:")
print(n)
print("You Account has been created")
print("Login")

