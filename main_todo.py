from password_for_todo_list import password
from task import task
def main():
    name=input ("hi welcome to todo ; whats your full name?")
    age=input("how old are you?")
    country=input("where are you from?")
    print(name,age,"from",country,"we are so happy you choosed our application ; we hope its usefull for you :) ")
    password()
    task()



if __name__ == "__main__":
    main()   
   