
drinks_menue={
        1:("latte",150),
        2:("moka",150),
        3:("americano",120),
        4:("espreso",120)
    }

# UI-only: add emojis and clean layout (no change to data or logic)
_EMOJI_MAP = {
    "latte": "☕",
    "moka": "☕",
    "americano": "☕",
    "espreso": "☕",
}

def drinks():
    # Styled heading using ANSI colors (terminal UI only)
    print("\n\033[95m╔══════════════════════════════════════════╗\033[0m")
    print("\033[1;33m   DRINKS - Gandom Coffee Shop\033[0m")
    print("\033[95m╚══════════════════════════════════════════╝\033[0m")
    for i in drinks_menue:
        name = drinks_menue[i][0]
        price = drinks_menue[i][1]
        emoji = _EMOJI_MAP.get(name, "🧋")
        # Preserve original name and price values; only change visual presentation
        print(f"{i}. {emoji} {name:<15} {price}")