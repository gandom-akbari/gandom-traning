def Institute_classes():
 n=0
 r=[]


 while n<1080:
  print("reserved classes",r)
  print("choose class from(a,b,c)")





  clas=input("class:") 
  if clas not in ["a","b","c"]:
   print("wrong information,try again")
   continue
  date=int(input("date:"))
  time=int(input("time:"))
  if date<1 or date>30 or time<9 or time>20 :
     print("wrong information,try again")
     continue 
  p=["class",clas,date,"at",time]
  n=n+1
  r.append(p)
  print("reservation is done secssufly")
  print("next")


 return(r)

if __name__ == "__main__":
 result=Institute_classes()
 print(result)


 
 
 
 