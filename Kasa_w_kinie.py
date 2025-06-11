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
print("-------MENU-------")
for item, data in menu.items():
    print(f"{item:10}: ${data['price']:.2f} , {data['stock']} in stock")
print("------------------")

# Pętla do składania zamówienia
while True:
    food = input("Select item (q to quit): ").lower()
    if food == "q":
        break
    if food not in menu:
        print("Item not found.")
        continue

    item = menu[food]
    price = item["price"]
    stock = item["stock"]

    try:
        quantity = int(input("How many? "))
        if quantity <= 0:
            print("Quantity must be at least 1.")
            continue
        if quantity > stock:
            print(f"Sorry, we have only {stock} in stock.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    cart[food] = cart.get(food, 0) + quantity
    menu[food]["stock"] -= quantity
    print("Item added to cart.\n")

# Podsumowanie zamówienia
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