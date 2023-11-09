import random

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ").lower()

rand_num = random.randint(0, 2)
if rand_num == 0:
    COMPUTER = "rock"
elif rand_num == 1:
    COMPUTER = "paper"
else:
    COMPUTER = "scissors"
print(f"Computer selects {COMPUTER}")

if player1 == COMPUTER:
    print("Its a tie!")

elif player1 == "rock":
    if COMPUTER == "scissors":
        print("Player wins!")
    else:
        print("Computer wins!")

elif player1 == "paper":
    if COMPUTER == "rock":
        print("Player wins!")
    else:
        print("Computer wins!")

elif player1 == "scissors":
    if COMPUTER == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")

else:
    print("Something went wrong")
