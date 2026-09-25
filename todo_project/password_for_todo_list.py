import re
def password():
    number=0
    name=input ("hi welcome to todo ; whats your full name?")
    age=input("how old are you?")
    country=input("where are you from?")
    print(f"\n========================================\n* Welcome, {name}! *\nAge: {age}\nCountry: {country}\n----------------------------------------\nThank you for choosing our application. We hope it is useful for you!\n========================================\n")
    print("\nPassword setup: Please create a password for your information security.\n----------------------------------------")
    while True:
     pas=input("Remember your pass should have 6-12 charecters including capital-small-nums ; " \
     "enter your password please=")
     num=re.search("\d",pas) 
     smal_num=re.search("[A-Z]",pas)
     capital=re.search("[a-z]",pas)
     n=len(pas)
     if n>=6 and n<=12 and num and smal_num and capital:
        print("\n========================================\nSUCCESS: Your secure passkey has been created.\n========================================\n")
        try:
            with open("todo.txt", "r") as file:
                existing_users = file.read().splitlines()
        except FileNotFoundError:
            existing_users = []

        number = 1
        for line in existing_users:
            if line.startswith("User "):
                try:
                    user_number = int(line.replace("User ", "").strip())
                    if user_number >= number:
                        number = user_number + 1
                except ValueError:
                    pass

        with open("todo.txt", "a") as file:
            file.write(f"\n{'=' * 50}\n")
            file.write(f"User {number}\n")
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Country: {country}\n")
            file.write(f"Password: {pas}\n")
            file.write(f"{'=' * 50}\n")
 
        break
     else:
        print("\nTry again. Make sure your password matches the required rules.\n----------------------------------------")

