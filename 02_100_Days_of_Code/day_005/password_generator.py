''' Day 6 Challenge '''
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator')

number_of_letters = int(input('How many letters woulld you like in your password? '))
number_of_symbols = int(input('How many symbols would you like? '))
number_of_numbers = int(input('How many nummbers would you like? '))

password = ''
#Eazy Level - Order not randomised:
#e.g. 3 letter, 2 symbol, 2 number = JduE&!91
for i in range(number_of_letters):
    password += random.choice(letters)

for i in range(number_of_symbols):
    password += random.choice(symbols)

for i in range(number_of_numbers):
    password += random.choice(numbers)

print(f'Here is your (easy) password: {password}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
l = list(password)
random.shuffle(l)
password = ''.join(l)

print(f'Here is your (hard) password: {password}')
