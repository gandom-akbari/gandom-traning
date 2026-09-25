
pizza_menu={
        1:("peperoni",500),
        2:("italian",500),
        3:("shikago",500),
        4:("california",500)
    }


def pizza():
    print("\n\033[95m╔══════════════════════════════════════════╗\033[0m")
    print("\033[1;36m   PIZZA - Gandom Coffee Shop\033[0m")
    print("\033[95m╚══════════════════════════════════════════╝\033[0m")

    for i in pizza_menu:
     print (i,pizza_menu[i][0],pizza_menu[i][1])



    