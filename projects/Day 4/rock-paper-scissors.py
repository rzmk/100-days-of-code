import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the Rock Paper Scissors tournament!")
user = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
user = int(user)

cpu = random.randint(0, 2)
rock_num = 0
paper_num = 1
scissors_num = 2

if user == rock_num and cpu == paper_num:
  print(f"{rock}\nComputer chose paper:\n{paper}\nYou lose.")
elif user == rock_num and cpu == scissors_num:
  print(f"{rock}\nComputer chose scissors:\n{scissors}\nYou win!")
elif user == rock_num and cpu == rock_num:
  print(f"{rock}\nComputer chose rock:\n{rock}\nDraw.")
elif user == paper_num and cpu == rock_num:
  print(f"{paper}\nComputer chose rock:\n{rock}\nYou win!")
elif user == paper_num and cpu == scissors_num:
  print(f"{paper}\nComputer chose scissors:\n{scissors}\nYou lose.")
elif user == paper_num and cpu == paper_num:
  print(f"{paper}\nComputer chose paper:\n{paper}\nDraw.")
elif user == scissors_num and cpu == rock_num:
  print(f"{scissors}\nComputer chose rock:\n{rock}\nYou lose.")
elif user == scissors_num and cpu == paper_num:
  print(f"{scissors}\nComputer chose paper:\n{paper}\nYou win!")
elif user == scissors_num and cpu == scissors_num:
  print(f"{scissors}\nComputer chose scissors:\n{scissors}\nDraw.")
