# Simple Conversions

initial_weight = float(input("Enter your weight: "))
initial_unit = input("Enter a unit (Kgs or Lbs): ")

weight = initial_weight
unit = initial_unit

if unit == "Kgs":
    weight = weight * 2.205
    unit = "Lbs."
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "Kgs."
else:
    print(f"{unit} is not a valid unit")
    exit()

print(f"Initial weight is: {initial_weight} {initial_unit}")
print(f"Converted weight is: {round(weight, 2)} {unit}")
