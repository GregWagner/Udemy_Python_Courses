name = input('Please enter your name: ')
age = int(input("How old are you, {}? ".format(name)))

if age >= 18:
    print('You are old enough to vote.')
    print('Please put an X in the box')
else:
    print("Please come back in {} years.".format(18 - age))

guess = int(input("Please guess a number between 1 and 10: "))
if guess < 5:
    guess = int(input('Please guess higher: '))
    if guess == 5:
        print('Well done, you guessed it')
    else:
        print('Sorry, you have not guessed correctly')
elif guess > 5:
    guess = int(input('Please guess lower: '))
    if guess == 5:
        print('Well done, you guessed it')
    else:
        print('Sorry, you have not guessed correctly')
else:
    print('Well done, you got it the first time')
