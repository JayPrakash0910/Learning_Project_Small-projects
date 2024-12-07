import string
import random

characters =list(string.ascii_letters+string.digits+"!@#$%^&*()")

def generate_password():
    password_lenght =int(input("how long would you like your password to be ?"))

    random.shuffle(characters)
    password =[]
    for x in range(password_lenght):
        password.append(random.choice(characters))
    random.shuffle(password)
    password ="".join(password)    
    print(password)
option =input("do you want to generated a password (yes/no) : ")
if option=="yes":
    generate_password()
elif option=="no":
    print("ended program")
    quit()
else:  
    print("invalid input , please inputor no")
    quit()  
