############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 21): # cannot be 20, as that would be out of bounds
    if i == 20:
      print("You got it")
my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # range includes both endpoints
print(dice_imgs[dice_num])

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994: # make sure 1994 itself is accounted for
  print("You are a Gen Z.")

# # Fix the Errors
age = input("How old are you?")
if int(age) > 18: # cast age
    print(f"You can drive at age {age}.") # indent within if statement, and make sure to put f for f string

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # remember = (declaration) is different from == (conditional)
total_words = pages * word_per_page
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # watch your indent!
  print(b_list)

mutate([1,2,3,5,8,13])