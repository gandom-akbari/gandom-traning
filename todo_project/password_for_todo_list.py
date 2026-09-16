import re
def password():
    number=0
    name=input ("hi welcome to todo ; whats your full name?")
    age=input("how old are you?")
    country=input("where are you from?")
    print(name,age,"from",country,"we are so happy you choosed our application ; we hope its usefull for you :) ")
    print(" please make a password for your information secretory")
    while True:
     pas=input("Remember your pass should have 6-12 charecters including capital-small-nums ; " \
     "enter your password please=")
     num=re.search("\d",pas) 
     smal_num=re.search("[A-Z]",pas)
     capital=re.search("[a-z]",pas)
     n=len(pas)
     if n>=6 and n<=12 and num and smal_num and capital:
        print("Amazing;now you have a passkey")
        with open("todo.txt", "a") as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Country: {country}\n")
            file.write(f"Password: {pas}\n")
            number +=1

        break
     else:
        print("try again honey ")

