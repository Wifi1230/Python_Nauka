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

def betting(wallet):
    while True:
        bet_size=(input("How much do you want to bet or type q to exit: "))
        if bet_size=="q":
            return wallet,None
        if bet_size.isdigit()==False:
            print("You need to pick a numeric value")
            continue
        if float(bet_size)>wallet:
            print(f"You can't bet {bet_size}$, you only have {wallet:.2f}$")
            continue
        bet_size=float(bet_size)
        wallet-=bet_size
        return wallet,bet_size

def pick():
    while True:
        pick=input("On wich number do you want to bet: ")
        if pick.isdigit() and int(pick)>=1 and int(pick)<=6:
            pick=int(pick)
            break 
        print("You need to pick number between 1 and 6")
    return pick

def roll(dice):
    for die in range(num_of_dice):
        dice.append(random.randint(1,6))
    print()
    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line] ,end="")
        print()


def dice_roll(wallet):
    while True:
        dice=[]
        right=0

        wallet,bet_size=betting(wallet)
        if bet_size is None:
            print("Thanks for playing dice!")
            break

        pick_int=pick()

        roll(dice)

        for die in dice:
            if die == pick_int:
                right+=1
        if right>0:
            right+=1
        profit=bet_size*right*0.9
        wallet+=profit
        if profit>0:
            print(f"You won {profit:.2f}$")
        else:
            print(f"You lose {bet_size}$")
        print(f"Your new ballance is {wallet:.2f}$")
    return wallet
