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

import random

game_images = [rock, paper, scissors]

user_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(game_images[user_choice])
computer_choice= random.randint(0,2)
print(game_images[computer_choice])
if user_choice== 0 and computer_choice==2:
  print('you win')
elif user_choice== 2 and computer_choice==1:
  print('you win')
elif user_choice==2 and computer_choice== 1:
  print('you win')
elif user_choice== computer_choice:
  print('remis')
else:
  print('computer win')

