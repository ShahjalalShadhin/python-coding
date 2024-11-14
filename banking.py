# Simple Banking program using python

def show_balance(balance):
    print(f"Your balance is {balance}tk")

def deposit_money():
    amount = int(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    else:
        return amount

def withdraw_money(balance):
    amount = int(input("Enter an amount to withdraw: "))

    if amount > balance:
        print("Insufficient amount.")
        return 0
    elif amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit_money()
        elif choice == "3":
            balance -= withdraw_money(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using our banking program!")

if __name__ == "__main__":
    main()

