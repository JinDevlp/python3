# Storing Dictionary inside a Dictionary using user inputs

account_list = {0: {"Name": "Owner", "Pin": 1234, "Balance": 100},
                }


def add_to_account_list(account_list):
    name = input("enter name: ").title()
    pin = int(input("enter pin: "))
    balance = 0
    account_list[len(account_list)] = {
        "Name": name, "Pin": pin, "Balance": balance}


on_off = True
while on_off:
    should_continue = input(
        "Would you like to add new user into the data? y or n: ")
    if should_continue == "y":
        add_to_account_list(account_list)
        print(account_list)
    else:
        on_off = False
for i in range(len(account_list)):
    if "Jin" in account_list[i]["Name"]:
        print(account_list)

account_list[0]["Name"] = "Joe"
print(account_list)
