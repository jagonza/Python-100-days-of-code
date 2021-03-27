import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money": 0,
}

commands = ["off", "report", "refill"]
for option in MENU:
    commands.append(option)


def execute_action(action):
    if action == "off":
        turn_off()
    elif action == "report":
        print_report()
    else:
        process_coffe(action)


def turn_off():
    print("Turning off...")
    sys.exit()


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    start()


def process_coffe(type):
    can_continue = check_for_resources(type)
    if can_continue:
        total = process_coins(type)
        update_resources(type)
        if total > MENU[type]["cost"]:
            change = total - MENU[type]["cost"]
            print(f"Here is ${change} in change.")
            print(f"Here is your {type} ☕️. Enjoy!")

    start()


def update_resources(type):
    water_nedded = MENU[type]["ingredients"]["water"]
    coffee_nedded = MENU[type]["ingredients"]["coffee"]
    milk_nedded = 0
    if "milk" in MENU[type]["ingredients"]:
        milk_nedded = MENU[type]["ingredients"]["milk"]

    resources["water"] -= water_nedded
    resources["coffee"] -= coffee_nedded
    resources["milk"] -= milk_nedded
    resources["money"] += MENU[type]["cost"]


def check_for_resources(type):
    water_nedded = MENU[type]["ingredients"]["water"]
    coffee_nedded = MENU[type]["ingredients"]["coffee"]
    milk_nedded = 0
    if "milk" in MENU[type]["ingredients"]:
        milk_nedded = MENU[type]["ingredients"]["milk"]

    water_remaining = resources["water"]
    coffee_remaining = resources["coffee"]
    milk_remaining = resources["milk"]

    if water_nedded > water_remaining:
        print("Sorry there is not enough water.")
        return False
    elif coffee_nedded > coffee_remaining:
        print("Sorry there is not enough coffee.")
        return False
    elif milk_nedded > milk_remaining:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True


def process_coins(type):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total_cents = (25 * quarters) + (10 * dimes) + (5 * nickles) + pennies
    total = total_cents / 100

    if total < MENU[type]["cost"]:
        print(f"Sorry ${total} are not enough. Money refunded.")
        return 0
    else:
        return total


def start():
    options = "What would you like? ("
    for option in MENU:
        options += f"{option} - ${MENU[option]['cost']} / "
    options = options[:-3]
    options += "): "
    command = input(options)

    if command not in commands:
        print(f"Sorry '{command}' is not a valid command")
    else:
        execute_action(command)


start()
