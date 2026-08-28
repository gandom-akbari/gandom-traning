def task():
   x=input("enter your task name ===> ")
   print (x)

   l=[ 
     ]
   number=1
   while True:
    task=input("my plans=")
    if task!="done":
     l.append(str(number)+" "+task)
    print("\n".join(l))
    
    number=number+1
    if task=="done":
      break
    


