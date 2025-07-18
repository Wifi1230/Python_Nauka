import random

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
        print(f"Your cards: {player_cards}")
    return wallet
