# Function that taked a parameter of Dictionary called "inches_snow"
# Use a for loop to iterate over the values of inches of snow in the dictionary and add it to the variable called total_inches
# Store user input as key:value into inches_snow Dictionary

# Created 1st week of July 2022

inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow.values():
        total_inches += inches
    print(f"Total snowfall inches: {total_inches}")


print_total_snowfall(inches_snow)

question = int(input("How many inches of snow fell on Thursday?: "))
inches_snow["Thursday"] = question
print_total_snowfall(inches_snow)
print(inches_snow)
