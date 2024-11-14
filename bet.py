# Slot Machine Program

import random
import time

def spin():
    symbols = ["🍒","🍉","🍋","🔔","⭐"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("*************")
    print(" | ".join(row))
    print("*************")

def payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 8
        elif row[0] == "🔔":
            return bet * 12
        if row[0] == "⭐":
            return bet * 20
    return 0

def main():
    balance = 1000
    
    print("************************")
    print("Welcome to Python Slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("************************")

    while balance > 0:
        print(f"Current Balance: {balance}tk")

        bet = input("Place your bet: ")

        if not (bet.lstrip("-").isdigit() and (bet.startswith("-") or bet.isdigit())):
            print("Invalid bet. Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient balance. Please try again.")
            continue

        if bet <= 0:
            print("Invalid bet. Please enter a positive number.")
            continue

        balance -= bet

        print("***Spinning***")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        row = spin()
        print_row(row)

        payment = payout(row, bet)
        if payment > 0:
            print(f"Congratulations! You won {payment}tk")
        else:
            print("Sorry, you lost the round.")

        balance += payment

        play_again = input("Do you want to play again (Y/N): ").upper()

        if play_again != "Y":
            break

    print("**********************************************")
    print(f"Game over! Your Final Balance is: {balance}tk")
    print("**********************************************")


if __name__ == "__main__":
    main()
