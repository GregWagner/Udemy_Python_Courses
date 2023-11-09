import random

highest = 10
answer = random.randint(1, highest)

print(f'Please guess a number between 1 and {highest}: ')
guess = int(input())
while guess != answer:
    if (guess == 0):
        print('See you next time')
        break
    if guess < answer:
        print('Please guess higher')
    else:
        print('Please guess lower')
    guess = int(input())

if guess == answer:
    print('You guessed the number')
