from art import logo
# from replit import clear
import random

program_end = False

def continue_blackjack():
    program_end = False
    while program_end == False:
        user_hand.append(random.choice(cards))
        user_sum = sum(user_hand)
        print(f"Your cards: {user_hand}, current score: {user_sum}")
        print(f"Computer's first card: {computer_hand[0]}")
        if user_sum > 21:
            return        
        ask_continue = input("Type 'y' to get another card, type 'n' to pass: ")
        if ask_continue == "y":
            continue_blackjack()
        else:
            program_end = True
    return

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_hand = []
user_hand.append(random.choice(cards))
user_hand.append(random.choice(cards))
user_sum = sum(user_hand)
computer_hand = [random.choice(cards)]
computer_sum = computer_hand[0]

response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if response == "y":
    print(logo)
    print(f"Your cards: {user_hand}, current score: {user_sum}")
    print(f"Computer's first card: {computer_hand[0]}")
    ask_continue = input("Type 'y' to get another card, type 'n' to pass: ")
    if ask_continue == "y":
        continue_blackjack()
    else:
        program_end = True
elif response == "n":
    quit()

user_sum = sum(user_hand)
print(f"Your final hand: {user_hand}, final score: {user_sum}")
computer_total_cards = random.randint(0, len(user_hand))
if computer_total_cards > 0:
    for i in range(computer_total_cards-1):
        computer_hand.append(random.choice(cards))
computer_sum = sum(computer_hand)

print(f"Computer's final hand: {computer_hand}, final score: {computer_sum}")
if user_sum >= 21 and computer_sum >= 21:
    print("Tie! You both drew 21 or over!")
elif user_sum > 21:
    print("You went over. You lose!")
elif computer_sum > 21:
    print("Opponent went over. You win!")
else:
    if (21-user_sum) > (21-computer_sum):
        print("Computer is closer to 21. You lose!")
    else:
        print("You're closer to 21. You win!")