from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Instantiating objects from imported classes
my_coffee_menu = Menu()
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

# Begin coffee machine with OOP!
response = ""
while response != "off":
    menu_items = my_coffee_menu.get_items()
    response = input(f"What would you like? ({menu_items}): ")
    if response == "off":
        break
    elif response == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_coffee_menu.find_drink(response)
        drink_cost = drink.cost
        if not my_coffee_maker.is_resource_sufficient(drink):
            print(f"Sorry there is not enough ingredients for {response}.")
            continue
        if not my_money_machine.make_payment(drink_cost):
            continue
        my_coffee_maker.make_coffee(drink)
