import random
import time

deck=[]

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10,'A': 11 
}
def create_deck():
    global deck
    deck = [
    '2♤', '3♤', '4♤', '5♤', '6♤', '7♤', '8♤', '9♤', '10♤', 'J♤', 'Q♤', 'K♤', 'A♤',
    '2♡', '3♡', '4♡', '5♡', '6♡', '7♡', '8♡', '9♡', '10♡', 'J♡', 'Q♡', 'K♡', 'A♡',
    '2♢', '3♢', '4♢', '5♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'J♢', 'Q♢', 'K♢', 'A♢',
    '2♧', '3♧', '4♧', '5♧', '6♧', '7♧', '8♧', '9♧', '10♧', 'J♧', 'Q♧', 'K♧', 'A♧'
    ]
    random.shuffle(deck)

def draw_card():
    global deck
    if not deck:
        create_deck()
    return deck.pop() if deck else None

def calculate_hand_value(hand):
    value=0
    aces=0
    for card in hand:
        rank=card[:-1]
        card_val=card_values.get(rank,0)
        value+=card_val
        if rank == 'A':
            aces+=1
    while value>21 and aces>0:
        value-=10
        aces-=1
    return value

def is_blackjack(hand):
    return calculate_hand_value(hand) == 21 and len(hand) == 2

def black_jack(wallet):
    while True:
        player_cards=[]
        dealer_cards=[]

        bet_size=input("How much do you want to bet? (press q to exit blackjack):")
        if bet_size=="q":
            break
        if not bet_size.isdigit():
            print("You need to enter a numeric value")
            continue
        bet_size=float(bet_size)
        if bet_size>wallet:
            print(f"You have only {wallet}$")
            continue
        

        if not deck:
            create_deck()

        for _ in range (2):
            player_cards.append(draw_card())
            dealer_cards.append(draw_card())

        print(f"Dealer cards: [{dealer_cards[0]}, '?']")
        print(f"Your cards: {player_cards} ({calculate_hand_value(player_cards)})")

        if is_blackjack(player_cards) and is_blackjack(dealer_cards):
            print("Push (draw). No money won or lost.")
            continue

        elif is_blackjack(player_cards):
            print(f"You have black jack, you won {bet_size*2.5}$")
            wallet+=bet_size*1.5
            print(f"Your ballance is {wallet}$")
            continue

        elif is_blackjack(dealer_cards):
            print(f"Dealer's cards: {dealer_cards}")
            print(f"Dealer have black jack you lose {bet_size}$")
            wallet-=bet_size
            print(f"Your ballance is {wallet}$")
            continue

        while True:
            action = input("Do you want to (h)it or (s)tand?: ").lower()
            if action == 'h':
                time.sleep(1)
                player_cards.append(draw_card())
                print(f"Your cards: {player_cards} ({calculate_hand_value(player_cards)})")
                if calculate_hand_value(player_cards) > 21:
                    print(f"Bust! You lose {bet_size}$")
                    wallet -= bet_size
                    print(f"Your ballance is {wallet}$")
                    break
            elif action == 's':
                break
            else:
                print("Invalid input. Type 'h' to hit or 's' to stand.")
        if calculate_hand_value(player_cards) > 21:
            continue

        player_value = calculate_hand_value(player_cards)
        dealer_value = calculate_hand_value(dealer_cards)

        time.sleep(1)
        while dealer_value < 17:
            print(f"Dealer's cards: {dealer_cards} ({dealer_value})")
            dealer_cards.append(draw_card())
            dealer_value = calculate_hand_value(dealer_cards)
            time.sleep(1)
            print(f"Dealer draws: {dealer_cards[-1]}")
            time.sleep(1)
            

        print(f"Dealer's final hand: {dealer_cards} ({dealer_value})")
        print(f"Your final hand: {player_cards} ({player_value})")

        # Result
        
        if dealer_value > 21 or player_value > dealer_value:
            print(f"You win {bet_size}$")
            wallet += bet_size
            print(f"Your ballance is {wallet}$")
        elif player_value < dealer_value:
            print(f"You lose {bet_size}$")
            wallet -= bet_size
            print(f"Your ballance is {wallet}$")
        else:
            print("Push (draw). No money won or lost.")
    return wallet
