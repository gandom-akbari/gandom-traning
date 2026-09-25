
cakes_menu={
          1:("choklate",200),
          2:("notella",200),
          3:("orange cake",200),
          4:("cream pie",200)
             }

# UI-only: emojis and nicer listing
_EMOJI_MAP = {
    "choklate": "🍰",
    "notella": "🍰",
    "orange cake": "🍰",
    "cream pie": "🍰",
}

def cakes():
    print("\n\033[95m╔══════════════════════════════════════════╗\033[0m")
    print("\033[1;35m   CAKES - Gandom Coffee Shop\033[0m")
    print("\033[95m╚══════════════════════════════════════════╝\033[0m")
    for i in cakes_menu:
        name = cakes_menu[i][0]
        price = cakes_menu[i][1]
        emoji = _EMOJI_MAP.get(name, "🍰")
        print(f"{i}. {emoji} {name:<18} {price}")




  
    