# Definicja menu - słownik zawierający dostępne produkty, ich ceny i ilość w magazynie
menu = {
    "pizza": {"price": 3.00, "stock": 10},
    "nachos": {"price": 4.50, "stock": 5},
    "popcorn": {"price": 6.00, "stock": 12},
    "fries": {"price": 2.50, "stock": 7},
    "chips": {"price": 1.00, "stock": 6},
    "pretzel": {"price": 3.50, "stock": 2},
    "soda": {"price": 3.00, "stock": 18},
    "lemonade": {"price": 4.25, "stock": 8}
}

cart = {}
total = 0

# Wyświetlenie menu
def menuprint():
    print("-------MENU-------")
    for item, data in menu.items():
        print(f"{item:10}: ${data['price']:.2f} , {data['stock']} in stock")
    print("------------------")

def cartprint():
    print("-----YOUR CART-----")
    for food, quantity in cart.items():
        price = menu[food]["price"]
        subtotal = price * quantity
        print(f"{quantity:3} x {food:12}: ${subtotal:.2f}")   

menuprint()

# Pętla do składania zamówienia
while True:
    food = input("Select item (or type q to quit, c to see the cart, m to see menu): ").lower()
    if food == "q":
        break
    elif food=="c":
        cartprint()
        continue
    elif food=="m":
        menuprint()
        continue
    if food not in menu:
        print("Item not found.")
        continue

    item = menu[food]
    price = item["price"]
    stock = item["stock"]

    try:
        quantity = int(input("How many?(type negative value if you want less than you have in cart or type 0 if you want to delete that position from order) "))
        if quantity == 0:
            cart.pop(food, None)
            print(f"{food} has been removed from your cart.")
            continue
        current_quantity = cart.get(food, 0)
        new_quantity = current_quantity + quantity
        if cart.get(food)!=None:
            if quantity+int(cart[food]) > stock:
                print(f"Sorry, we have only {stock} in stock.")
                continue
            elif quantity > stock:
                print(f"Sorry, we have only {stock} in stock.")
                continue
            elif abs(quantity)>int(cart[food]):
                cart.pop(food)
                continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    cart[food] = cart.get(food, 0) + quantity
    print("Item added to cart.\n")

print("-----YOUR ORDER-----")
for food, quantity in cart.items():
    price = menu[food]["price"]
    subtotal = price * quantity
    total += subtotal
    print(f"{quantity:3} x {food:12}: ${subtotal:.2f}")

# Rabat 10% jeśli total >= 20
discount = total * 0.1 if total >= 20 else 0
if discount > 0:
    print(f"{'Discount':17}: -${discount:.2f}")

print("------------------")
print(f"{'Total to pay':17}: ${total - discount:.2f}")
