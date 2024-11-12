import random

lowest_value = 1
highest_value = 100
answer = random.randint(lowest_value, highest_value)
guesses = 0
is_running = True

print("----PYTHON NUMBER GUESSING GAME!----")
print(f"Enter a number between {lowest_value} and {highest_value}")

while is_running:
    guess = input("Enter your guess: ")

    if (guess.lstrip("-").isdigit() and (guess.startswith("-") or guess.isdigit())):
        guess = int(guess)
        guesses += 1

        if guess < lowest_value or guess > highest_value:
            print("That number is out of range.")
            print(f"Please, Enter a number between {lowest_value} and {highest_value}")
        elif guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number.")
            print(f"It took you {guesses} attempts.")
            is_running = False               

    else:
        print("Invalid Guess!")
        print(f"Please, Enter a number between {lowest_value} and {highest_value}")
