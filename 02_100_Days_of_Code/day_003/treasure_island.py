print('|                   |  ,-"_,=""     `"=.|                  |')
print('|___________________|__"=._o`"-._        `"=.______________|___________________')
print('          |                `"=._o`"=._      _`"=._                     |')
print(' _________|_____________________:=._o "=._."_.-="\'"=.__________________|_______')
print('|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |')
print('|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'__|___________________')
print('          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |')
print(' _________|___________| ;`-.o`"=._; ." ` \'`."\` . "-._ /_______________|_______')
print('|                   | |o;    `"-.o`"=._``  \'` " ,__.--o;   |')
print('|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________')
print('____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____')
print('/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_')
print('____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____')
print('/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_')
print('____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____')
print('/______/______/______/______/______/______/______/______/______/______/_____ /')
print('*******************************************************************************')
print()
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')

user_input = input('Do you want to go [L]eft or [Right]: ')
if user_input != 'L':
    print('You fell into a hole and died...')
else:
    user_input = input('Do you want to swim or wait: ')
    if user_input != 'wait':
        print('You were attacked by a trout and died...')
    else:
        user_input = input('Do you want to enter the [R]ed or [B]lue or [Y]ellow door: ')
        if user_input == 'R':
            print('You were burned by fire and died...')
        elif user_input == 'B':
            print('You were eaten by beasts and died...')
        elif user_input == 'Y':
            print('You won...')
        else:
            print('Game over')




