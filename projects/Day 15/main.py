# imports
from data import menu, resources

# coffee machine logic
def coffee_machine():
    response = ""
    profit = 0.00
    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']
    while response != "off":
        money = 0.00
        response = input("What would you like? (espresso/latte/cappuccino): ")
        if response == "report":
            print(f"Water: {water_left}ml")
            print(f"Milk: {milk_left}ml")
            print(f"Coffee: {coffee_left}g")
            print(f"Profit: ${profit}")
        elif response == "espresso" or response == "latte" or response == "cappuccino":
            cost = menu[response]['cost']
            for ingredient in menu[response]['ingredients']:
                if resources[ingredient] < menu[response]['ingredients'][ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    continue
            print("Please insert coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickles = float(input("How many nickles?: "))
            pennies = float(input("How many pennies?: "))
            money += 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
            if money < cost:
                print("Sorry that's not enough money. Money refunded.")
                continue
            profit += cost
            water_left -= menu[response]['ingredients']['water']
            coffee_left -= menu[response]['ingredients']['coffee']
            if 'milk' in menu[response]['ingredients']:
                milk_left -= menu[response]['ingredients']['milk']
            money -= cost
            print(f"Here is ${money} in change.")
            print(f"Here is your {response} ☕. Enjoy!")
        elif response == "off":
            break
        else:
            print("Please select a valid item.")
    exit()

# start coffee machine
coffee_machine()