def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() != 'y':
            print("Thank you for using the calculator!")
            break

# Run the calculator
calculator()