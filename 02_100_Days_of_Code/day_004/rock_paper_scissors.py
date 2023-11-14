''' Day 4 Challenge '''
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
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

ROCK = 0
PAPER = 1
SCISSORS = 2

user_choice = int(input('What do you choose? Type 0 or Rock, 1 for Paper, or 2 for Scissors. '))
while user_choice < ROCK or user_choice > SCISSORS:
    print('Illegal selection')
    user_choice = int(input('What do you choose? Type 0 or Rock, 1 for Paper, or 2 for Scissors. '))

print(game_images[user_choice])
computer_choice = random.randint(1, 3)
print('Computer chose:')
print(game_images[computer_choice])


if user_choice == computer_choice:
    print("Game is tied")
elif user_choice == ROCK:
    if computer_choice == PAPER:
        print('Computer wins')
    else:
        print('Player wins')
elif user_choice == PAPER:
    if computer_choice == SCISSORS:
        print('Computer wins')
    else:
        print('Player wins')
else:
    if computer_choice == ROCK:
        print('Computer wins')
    else:
        print('Player wins')