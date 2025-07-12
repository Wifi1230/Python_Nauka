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
bettings={}

def betting(wallet):
    while True:
        bet_size=(input("How much do you want to bet: "))
        if bet_size.isdigit()==False:
            print("You need to pick a numeric value")
            continue
        if float(bet_size)>wallet:
            print(f"You can't bet {bet_size}$, you only have {wallet:.2f}$")
            continue
        
        bet_size=float(bet_size)
        choice=pick()
        if choice in bettings:
            bettings[choice] += bet_size
        else:
            bettings[choice] = bet_size
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
        total_payout=0
        final_betting_size=0
        play=input("Do you want to bet in this dice throw?(y/n or q to quit dice)")
        if play.lower()=="q":
            break
        if play.lower()!="yes" and play.lower()!="y":
            roll(dice)
            continue
        while True:
            wallet,bet_size=betting(wallet)
            more=input("Do you want to bet on one more option?(y/n):")
            if more.lower()!="yes" and more.lower()!="y":
                break


        # pick_int=pick()

        roll(dice)
        for pick_int,bet_size in bettings.items():
            final_betting_size+=bet_size
            right=0
            for die in dice:
                if die == pick_int:
                    right+=1
            if right>0:
                total_payout+=bet_size*right*0.9+bet_size
        wallet+=total_payout
        if total_payout-final_betting_size>0:
            print(f"You won {total_payout-final_betting_size:.2f}$")
        else:
            print(f"You lose {final_betting_size-total_payout}$")
        print(f"Your new ballance is {wallet:.2f}$")
        bettings.clear()
    return wallet
