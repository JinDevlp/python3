# Simple number guessing game using a random module
# Created June 2022
import random


computer_number = random.randint(1, 15)
print("Pick a number from 0 to 15 ")


game_off = False
while not game_off:
    user_guess = int(input("Guess a number: "))
    if user_guess > computer_number:
        print(f"Your number, {user_guess} is too high")
    elif user_guess < computer_number:
        print(f"Your number, {user_guess} is too low")
    else:
        print(f"That's correct! Random number was {computer_number}. ")
        game_off = True
