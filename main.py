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


profit = 0
resources = {
    "water": 1000,
    "milk": 200,
    "coffee": 100,
}


# Print report of all coffee machine resources
def print_report():
    """Printing out amount of resources and profit when function is called"""
    for key, resource in resources.items():
        if key == "coffee":
            print(f"{key.title()}: {resource}g")
        else:
            print(f"{key.title()}: {resource}ml")
    print(f"Money: ${profit}")


# Check for resources sufficient before making coffee
def check_resources_sufficient(order_ingredients):
    """Return True when order can be made, False if not enough ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# Process coins. Insert different types coins and check if it's enough money
def process_coins(coffee, price):
    """Returns the total calculated from coins inserted"""
    print(f"Price for {coffee.title()}: ${price}")
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total_coins = quarters + dimes + nickles + pennies
    return total_coins


# Check if transaction is successful
def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Make coffee when sufficient resources and transaction successful
def make_coffee(drink_name, order_ingredients):
    """Deduct the required resources from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")


# Ask user what they want to drink as long as the coffee machine is on
machine_is_on = True
while machine_is_on:
    choice = input("What would you like to? (espresso/latte/cappuccino): ").lower()

    if choice == "report":
        print_report()
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[choice]
        if check_resources_sufficient(drink["ingredients"]):
            payment = process_coins(choice, drink["cost"])
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        machine_is_on = False
