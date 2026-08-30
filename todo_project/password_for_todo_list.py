import re
def password():
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
        break 
     else:
        print("try again honey ")

