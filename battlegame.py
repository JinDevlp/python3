# game info
# created by Jin July 02 2022
# Creating a simple game using while loop, variables and if/elif/else statements

# Characters
is_game_on = True
while is_game_on:
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    dragon = "Dragon"
    shreck = "Orc"

    # Characters hp
    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    dragon_hp = 300
    shreck_hp = 350

    # Characters damage
    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    dragon_damage = 50
    shreck_damage = 120

# Character selection
# print(f"1) {wizard}")
# print(f"2) {elf}")
# print(f"3) {human}")
# user_character = input("Choose your character: ")
# print(user_character)


# Handle player choice
    while True:
        print(f"1) {wizard}")
        print(f"2) {elf}")
        print(f"3) {human}")
        print(f"4) {shreck}")
        character = (input("Choose your character: ")).lower()
        if character == "1" or character == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif character == "2" or character == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break

        elif character == "3" or character == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif character == "4" or character == "shreck":
            character = shreck
            my_hp = shreck_hp
            my_damage = shreck_damage
            break
        else:
            print("Unknown character, Please pick again!")
    print(f"\nYou have chosen {character}.")
    print(f"Health: {my_hp}")
    print(f"Damage: {my_damage}\n")

# Battle with the Dragon
    while True:
        dragon_hp -= my_damage
        print(f"The {character} damaged the dragon! ")
        print(f"Dragon, HP: {dragon_hp}")
        if dragon_hp <= 0:
            print(f"The Dragon has lost the battle. {character} win")
            break
        my_hp -= dragon_damage
        print(f"The Dragon has damaged {character}")
        print(f"{character}, HP: {my_hp}")
        if my_hp == 0:
            print(f"{character} has lost the battle! ")
            break
    game_restart = input("Would you like to start the game? (y/n): ")
    if game_restart == 'n':
        is_game_on = False
