questions = ("What is the primary function of chlorophyll in plants?: ",
             "Which of the following particles has no electrical charge?: ",
             "Which of the following laws explains why a rocket moves forward when it expels gas backward?: ",
             "Which element is most abundant in the Earth's atmosphere?: ",
             "What is the pH of pure water at 25°C?: ")

options = (("A. To absorb water from the soil","B. To convert carbon dioxide into oxygen","C. To absorb light for photosynthesis","D. To transport nutrients in the plant"),
           ("A. Proton","B. Electron","C. Positron","D. Neutron"),
           ("A. Newton's First Law","B. Newton's Second Law","C. Newton's Third Law","D. Law of Conservation of Energy"),
           ("A. Oxygen","B. Nitrogen","C. Carbon dioxide","D. Argon"),
           ("A. 7","B. 0","C. 5","D. 14"))

answers = ("C",
           "D",
           "C",
           "B",
           "A")
guesses = []
score = 0
question_number = 0

for question in questions:
    print(".................................")
    print(question)
    for option in options[question_number]:
        print(option)
    
    guess = input("Enter your guess (A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_number]} is the correct answer.")
    
    question_number += 1


print("*************RESULT**************")

print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
