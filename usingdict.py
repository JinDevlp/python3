# More practice on Dictionary
# Created 2nd week of July 2022

# Dictionary
# {key: value, key:value}


user_settings = {"lang": "en-us", "platform": "Windows 10"}

print(user_settings["lang"])
# retrieve value of the key

orders = {5: "bbq", 2: "tacos", 9: "pizza"}
orders[9] = "tacos"

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# print(thisdict["brand"])

# Accessing items
x = thisdict["model"]

# Get the value of "model" key:
y = thisdict.get("model")

# Get a list of the keys:
z = thisdict.keys()
q = thisdict.values()
# print(z, q)

# Add key and value
thisdict["color"] = "red"

# print(thisdict)

# Get list of keys and value pairs:
pairs = thisdict.items()
# print(pairs)

# if "model" in thisdict:
# print("yes")


data = [{"Name": "Owner", "PIN": 1234,
         "Balance": 100},
        {
    "Name": "Jin", "PIN": 1111,
    "Balance": 200
}]
for element in data:
    user_name = element["Name"]
    user_pin = element["PIN"]
    user_balance = element["Balance"]
    if "Jin" in user_name:
        print("yes, Jin in the data.")

for x in thisdict.values():
    print(x)
for x in thisdict.keys():
    print(x)
for x, y in thisdict.items():
    print(x, y)

state_capitals = {"Washington": "Olympia",
                  "Oregon": "Salem", "California": "Sacramento"}
for state in state_capitals:
    print(state)

for city in state_capitals.values():
    print(city)

for state in state_capitals:
    print(state_capitals[state], "is the capital of", state)

for state, city in state_capitals.items():
    print(city, "is the capital of", state)
