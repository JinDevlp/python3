# Created by Jin Choi 4th week of June 2022

# iterating over the numbers starting from 0 increasing by 5 until it hits 100 using if/elif/else statements

for amount_loaded in range(0, 105, 5):
    if amount_loaded == 25:
        print(f"< {amount_loaded}% loaded > 1/4 of the way there.")
    elif amount_loaded == 50:
        print(f"< {amount_loaded}% loaded > 1/2 of the way there.")
    elif amount_loaded == 75:
        print(f"< {amount_loaded}% loaded > 3/4 of the way there.")
    elif amount_loaded == 100:
        print(f"< {amount_loaded}% loaded > Loading complete!")
    else:
        print(amount_loaded)
