menu={"pizza": {"price": 3.00, "stock": 10},
    "nachos": {"price": 4.50, "stock": 5},
    "popcorn": {"price": 6.00, "stock": 12},
    "fries": {"price": 2.50, "stock": 7},
    "chips": {"price": 1.00, "stock": 6},
    "pretzel": {"price": 3.50, "stock": 2},
    "soda": {"price": 3.00, "stock": 18},
    "lemonade": {"price": 4.25, "stock": 8}}
cart={}
total=0
print("-------MENU-------")
for key,value in menu.items():
    print(f"{key:10}: ${value.get('price'):.2f} ,{value.get('stock')} in stock")
print("------------------")
while True:
    food=input("Select item (q to quit): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        quantity=int(input("How many?"))
        if quantity<menu.get(food).get('stock'):
            cart.update({food:quantity})
        else:
            print(f"we have only {menu.get(food).get('stock')} in stock")
        print("")
print("-----YOUR ORDER-----")
for food,quantity in cart.items():
    total+=float(menu.get(food).get('price'))*int(quantity)
    print(f"{quantity:3} x {food:10}: ${float(menu.get(food).get('price'))*int(quantity):.2f}")
print("------------------")
print(f"Your total is ${total:.2f}")


