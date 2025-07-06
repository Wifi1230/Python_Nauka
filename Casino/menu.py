import diceroll

wallet=float(input("How much do you want to deposit: "))

while True:
    print("\n=== MENU ===")
    print("1. Dice")
    print("2. Show ballance")
    print("3. Exit casino")

    choice = input("Choose option: ")

    if choice == "1":
        wallet=diceroll.dice_roll(wallet)
    elif choice =="2":
        print(f"\nYour ballance is {wallet:.2f}$")
    elif choice == "3":
        print(f"Bye bye! Your payout is {wallet:.2f}$")
        break
    else:
        print("Wrong choice.")
