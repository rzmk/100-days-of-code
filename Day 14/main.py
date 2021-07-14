# imports
import replit
import random
import art
from game_data import data

# get new people
def load_people():
    a = random.choice(data)
    b = random.choice(data)
    while (b == a):
        b = random.choice(data)
    return a, b

# play game
def play():
    # setup variables
    score = 0
    is_start = True
    lost_game = False

    while True:
        replit.clear()
        print(art.logo)

        if is_start == False:
            print(f"You're right! Current score: {score}.")
        a, b = load_people()

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(art.vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        answer = input("Who has more followers? Type 'A' or 'B': ")

        # check answer
        if a['follower_count'] > b['follower_count'] and answer == "A":
            score += 1
            is_start = False
            continue
        elif a['follower_count'] > b['follower_count'] and answer == "B":
            break
        elif a['follower_count'] < b['follower_count'] and answer == "A":
            break
        else:
            score += 1
            is_start = False
            continue
    print(f"Sorry, that's wrong. Final score: {score}")

# run game
play()