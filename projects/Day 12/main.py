from random import randint
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
actual_answer = randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    guesses = 10
elif difficulty == "hard":
    guesses = 5

while guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number.")
    answer = input("Make a guess: ")
    if int(answer) < actual_answer:
        print("Too low.\nGuess again.")
    elif int(answer) > actual_answer:
        print("Too high.\nGuess again.")
    elif int(answer) == actual_answer:
        break
    guesses -= 1

if int(answer) == actual_answer:
    print(f"You got it! The answer was {actual_answer}.")
else:
    print("You've run out of guesses. You lose.")