name = input('Enter your name: ')
age = int(input('Enter you age, {}: '.format(name)))

if 18 < age < 31:
    print('Welcome to the holiday')
else:
    print('Sorry, you are not the correct age.')
