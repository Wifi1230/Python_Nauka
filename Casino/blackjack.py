import random

deck=[]
player_cards=[]
dealer_cards=[]

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

def black_jack(wallet):
    if not deck:
        create_deck()
    player_cards.clear()
    dealer_cards.clear()
    for draw in range (2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())
        draw+=1
    return wallet
