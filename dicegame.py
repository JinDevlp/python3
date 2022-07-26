# Random dice game competing with the computer
# Keep up with the high score

# Created 2nd week of July 2022
import random


high_score = 0
is_game_on = True
print(f"\nCurrent High Score: {high_score}")

while is_game_on:
    print("1) Roll Dice ")
    print("2) Leave Game ")
    choice = input("Enter your choice: ")
    computer1 = random.randint(1, 6)
    computer2 = random.randint(1, 6)
    if choice == '2':
        is_game_on = False
    elif choice == '1':
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        user_total = num1 + num2
        computer_total = computer1 + computer2
        print(f"\nYour first dice is a.... {num1}")
        print(f"Your second dice is a.... {num2}")
        print(f"\nComputer's first dice is a.... {computer1}")
        print(f"Computer's second dice is a.... {computer2}")
        print(f"\nYou rolled a total of {user_total}")
        print(f"\nComputer rolled a total of {computer_total}")
    if user_total > high_score and user_total > computer_total:
        high_score = user_total
        print("You achieved the high score")
    elif computer_total > high_score and computer_total > user_total:
        high_score = computer_total
        print("Computer achieved the high score")
    elif computer_total and user_total < high_score:
        print("No change in high score")
    print(f"\nCurrent High Score: {high_score}")
