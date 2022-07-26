# .append and .remove method to add and remove from list.

import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []


game_on = True
while game_on:
    user_card = input("'Enter' to pick a card or 'Q' to quit: ").lower()
    if user_card == "q":
        print("Good bye ")
        break
    else:
        user_card = random.choice(diamonds)
        diamonds.remove(user_card)
        hand.append(user_card)
        print(f"Your Cards: {hand}")
        print(f"Remaining Cards {diamonds}")
    if diamonds == []:
        game_on = False
        print("There are no more cards to pick.")
