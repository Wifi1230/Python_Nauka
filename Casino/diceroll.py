import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
num_of_dice=3

def dice_roll(wallet):
    while True:
        dice=[]
        right=0
        bet_size=(input("How much do you want to bet or type q to exit: "))
        if bet_size=="q":
            break
        elif float(bet_size)>wallet:
            print(f"You can't bet {bet_size}$, you only have {wallet}$")
            break
        else:
            bet_size=float(bet_size)
            wallet-=bet_size
        pick=int(input("On wich number do you want to bet: "))

        for die in range(num_of_dice):
            dice.append(random.randint(1,6))
        print()
        for line in range(5):
            for die in dice:
                print(dice_art.get(die)[line] ,end="")
            print()

        for die in dice:
            if die == pick:
                right+=1
        if right>0:
            right+=1
        profit=bet_size*right*0.85
        wallet+=profit
        if profit>0:
            print(f"You won {profit:.2f}$")
        else:
            print(f"You lose {bet_size}$")
        print(f"Your new ballance is {wallet:.2f}$")
    return wallet
