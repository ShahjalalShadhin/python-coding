menu = {"pizza": 550,
        "popcorn": 250,
        "soda": 60,
        "burger": 350,
        "fries": 150,
        "chips": 50}

cart = []
total = 0

print("------------ MENU ------------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}tk")
print("------------------------------")

while True:
    food = input("Select an item (e to exit): ").lower()
    if food == "e":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("--------- YOUR ORDER ---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your Total is: {total:.2f}tk")
print("------------------------------")
