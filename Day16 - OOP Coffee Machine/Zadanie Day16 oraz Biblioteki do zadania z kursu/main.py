from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
coin = MoneyMachine()

while is_on:
    choice = input(f"What would you like? {menu.get_items()} ").lower()

    if choice == "report":
        coffee_maker.report()
        coin.report()
    elif choice == "off":
        is_on = False
    elif choice in menu.get_items():
        coffee = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(coffee) and coin.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)
    else:
        print("Wrong choice!")
