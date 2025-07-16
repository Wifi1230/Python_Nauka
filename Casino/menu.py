import diceroll
import blackjack

while True:
    wallet=input("How much do you want to deposit: ")
    if wallet.isdigit():
        wallet=float(wallet)
        break
    print("You need to type a numeric value")

while True:
    print("\n=== MENU ===")
    print("1. 🎲 Play Dice")
    print("2. ♠️ Play Black Jack")
    print("3. 💰 Show Balance")
    print("4. 🚪 Exit Casino")

    choice = input("Choose option: ")

    if choice == "1":
        wallet=diceroll.dice_roll(wallet)
    elif choice=="2":
        wallet=blackjack.black_jack(wallet)
    elif choice =="3":
        print(f"\nYour balance is {wallet:.2f}$")
    elif choice == "4":
        print(f"Bye bye! Your payout is {wallet:.2f}$")
        break
    else:
        print("Wrong choice.")
