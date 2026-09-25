from coffe_menu.drink import drinks ,drinks_menue
from coffe_menu.cakes import cakes, cakes_menu
from coffe_menu.pizza import pizza, pizza_menu

menue={1:(drinks_menue,drinks),
       2:(cakes_menu,cakes),
       3:(pizza_menu,pizza),
       4:(exit,exit)}

r=[]



def main():
    price = 0
    # Clean, modern header (terminal styling only)
    print("\n\033[1;96m========================================\033[0m")
    print("\033[1;95m   Welcome to Gandom Coffee Shop ☕\033[0m")
    print("\033[1;96m========================================\033[0m\n")
    while True:
       choice=int(input("\n\033[1;92mMenu parts:\033[0m \n"
                        "1: drinks\n"
                        "2: cakes\n"
                        "3: pizza\n"
                        "4: exit\n"
                        "which one is your ideal part? "))
       if choice==4:
           print(r,"\n","total price is :",price)
           break
       selected_menu=menue[choice]
       selected_menu[1]()
       item=int(input("\n\033[1;93mChoose your item honey :\033[0m"))
       selected_item=selected_menu[0][item]
       print("\n\033[90mSelected:\033[0m",selected_item[0])
       print(selected_item[1])


       r.append((selected_item[0],selected_item[1]))
       print(r)
       for p in r:
        price+=p[1]





if __name__=="__main__":
 main()