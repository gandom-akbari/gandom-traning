from coffe_menu.drink import drinks
from coffe_menu.cakes import cakes
from coffe_menu.pizza import pizza





def main():
    while True:
       print("hi welcome to gandom coffeshop ")
       x= int(input("wich of the following item would you perefer?[1-drinks  2-cakes  3-pizza]>>>"))
       if x==1:
          print("------------------------")
          drinks()
       elif x==2:
            print("------------------------")
            cakes()
       elif x==3:
            print("------------------------")
            pizza()
         
       else:
            print("we dont havr that item now ; im sorry ")
       
         



if __name__=="__main__":
     main()