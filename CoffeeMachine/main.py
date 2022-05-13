# Ensures that the program main.py is ran when running the script

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

operation = True
status = "user"


def display_resources():
    """ Show report for resources"""
    for i in resources:
        if i == 'coffee':
            print(f"{i} : {resources[i]} g")
        else:
            print(f"{i} : {resources[i]} ml")


def compute(dollar, fifty, twenty, ten):
    """ Computes total money received """
    amt = 0
    amt = amt + (dollar * 1.0) + (fifty * 0.50) + (twenty * 0.20) + (ten * 0.10)
    return amt


def check_available_drink(data, resources, drink):
    """ Checks if drink can be served given resources """
    water, milk, coffee = resources["water"], resources["milk"], resources["coffee"]
    required = []
    for i in data[drink]["ingredients"].values():
        # required pertains to water, milk and coffee in that specific order
        required.append(i)
    return False if (water < required[0] or milk < required[1] or coffee < required[2]) else True


def deduct_resources(data, drink):
    """Directly changes resource levels after drink is dispensed"""
    global resources
    required = []
    for i in data[drink]["ingredients"].values():
        # required pertains to water, milk and coffee in that specific order
        required.append(i)
    resources["water"] -= required[0]
    resources["milk"] -= required[1]
    resources["coffee"] -= required[2]


if __name__ == '__main__':
    while operation:
        status = input("Are you a user or an administrator (user/admin)\n")
        if status == "user":
            user_input = input("What would you like to drink today? (expresso/latte/capuccino): ")
            if check_available_drink(MENU, resources, user_input):
                print(f"The cost of the drink you've selected will be {MENU[user_input]['cost']}")
            else:
                print("The drink you have chosen is not available due to insufficient "
                      "ingredients, resetting to start...")
                continue
            print("Please insert coins")
            dollar = int(input("# of dollar coins: "))
            fifty = int(input("# of fifty-cent coins: "))
            twenty = int(input("# of twenty-cent coins: "))
            ten = int(input("# of ten-cent coins: "))
            amount = compute(dollar, fifty, twenty, ten)
            print(f"You inserted ${amount}, dispensing ${amount - MENU[user_input]['cost']} in change...")
            deduct_resources(MENU, user_input)
            print(f"Here is your {user_input} ☕ Enjoy!")
        elif status == "admin":
            admin_input = input("Task Manager: What action would you like to perform (report/off): ")
            if admin_input == "off":
                print("Machine will be turned off, Goodbye.")
                break
            elif admin_input == "report":
                display_resources()
                continue







