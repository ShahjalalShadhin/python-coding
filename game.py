import random

options = ("rock", "paper", "scissors")
playing = True

print()
print("--- Welcome to Rock, Paper, Scissors! ---")

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper or scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    else:
        print("Computer wins!")
    
    if not input("Do you want to play again? (y/n): ").lower() == "y":
        playing = False

print()
print("--- Thanks for playing! ---")