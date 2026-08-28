import random
name=["gandom","nazi","elina","parmis","parsa","bil bil"]
present=["10$","50$","100$","500$","1000$","nothing"]
for i in name:
    y=random.choice(present)
    print (i,y)
    if y!="nothing":
        present.remove(y)
    print("==========================")


n=0
for i in range(20):
    f=random.randint(1,6)
    print(f)
    if f==6:
      n=n+1
print("______________________________")
print(n)      



