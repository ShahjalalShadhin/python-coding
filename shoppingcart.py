#Shopping Cart Program

items = []
prices = []
total = 0

while True:
    item = input("Enter an item (e to quit): ")
    if item.lower() == "e":
        break
    else:
        price = float(input(f"Enter the price of {item} (in tk): "))
        items.append(item)
        prices.append(price)

print("Your Items Are")

for item in items:
    print(item, end = " ")

for price in prices:
    total += price

print()
print(f"Total Price: {total}tk")
