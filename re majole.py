import re
pas="gandom akbari 123456789"
x=re.search("\D",pas)
if x:
        print("T")
else:
        print("F")


pasS="gandom akbari 123456789"
o=re.findall("[1-5]",pasS)
print(o)


pasSs="gandom akbari 123456789"
i=re.split("[\d]",pasSs)
print(i)    




pasSs="gandom akbari 123456789"
w=re.sub("\d","0",pasSs)
print(w)



while True:
   p=(str(input("hi there;please enter your new password=")))

   small=re.search ("[a-z]",p) 
   cpital=re.search("[A-Z]",p)
   charector=re.search("[$@#]",p)
   num=re.search ("[1-9]",p)   
   n=len(p)
   if n<=12 and n>=6 and small and cpital and charector and num:
        print("you remade your pass seccesfully")
        break
else:
        print ("oh im sorry;try again later ")







