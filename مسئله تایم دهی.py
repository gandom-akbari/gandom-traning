def moshaver():
    n=0
    y=[]
    while n<31:
        print("booked dates==",y)
        date=int(input("enter your date:"))
        if date<1 or date>30:
            print("eror,try again")
            continue
        if date in y:
            print("eror,try again")
            continue
        else:
            print("enter your information plrase :")
            fn=input("first name:")
            ln=input("last name:")
            num=input("phone number:")
            y=y+[date]
            n=n+1
moshaver()            