def booking_center():
 n=0
 r=[]

 
 while n<360:
  print("reserved datas",r)
  date=(input("enter your date="))
  time=(input("enter your time="))
  p=date+"at"+time
  date=int(date)
  time=int(time)


  if date<1 or date>30 or time<9 or time>21:
   print("wrong information,try again")
   continue


  if p in r:
     print("sorry this time is already booked , try another time ")
     continue 


  else:
    print("now enter your information")
    fname=input("first name=")
    lname=input("last name=")
    print("The reservation for",fname,lname,"in",p,"has been made.")
    n=n+1
    r=r+[p]



 return(r)

if __name__ == "__main__":
 result=booking_center()
print(result)
          

