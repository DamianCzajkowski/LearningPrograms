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
    "money": 0
}


class NoResourcesException(Exception):
    pass


class NotEnoughMoneyException(Exception):
    pass


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def validate_resources(choice):

    for key, value in MENU[choice]["ingredients"].items():
        if resources[key] < value:
            raise NoResourcesException(f"Sorry there is not enough {key}")
    return True


def process_coins(choice):
    print("Insert coins")
    quarter = int(input("Insert quarter: "))
    dimes = int(input("Insert dimes: "))
    nickel = int(input("Insert nickel: "))
    pennies = int(input("Insert pennies: "))
    sum_of_coins = quarter*0.25 + dimes*0.10 + nickel*0.05 + pennies * 0.01
    if sum_of_coins < MENU[choice]["cost"]:
        raise NotEnoughMoneyException("Sorry that's not enough money. Money refunded.")
    if sum_of_coins > MENU[choice]["cost"]:
        print(f"Here is ${sum_of_coins-MENU[choice]['cost']} dollars in change.")
    return MENU[choice]["cost"]


def made_coffee(choice):
    try:
        validate_resources(choice)
    except NoResourcesException as e:
        print(e)

    try:
        money = process_coins(choice)
        resources["money"] += money
    except NotEnoughMoneyException as e:
        print(e)

    for key, value in MENU[choice]["ingredients"].items():
        resources[key] -= value


def menu():
    while True:
        coffee_choice = input(
            f"What would you like? ({'/'.join(MENU.keys())}): \n")

        if coffee_choice == "off":
            return
        if coffee_choice == "report":
            print_report()

        if coffee_choice not in MENU.keys():
            print("There is no choice like that :)")
            continue

        made_coffee(coffee_choice)

        print(f"Here is your {coffee_choice}. Enjoy!")


if __name__ == "__main__":
    menu()
