from CoffeeMachine import CoffeeMaker

machine_working = True

while machine_working:

    user_choice = input("What would you like? (espresso/latte/cappuccino: ").lower()
    coffee = CoffeeMaker()
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        chosen_coffee = coffee.get_coffee(user_choice)

    if user_choice == 'report':
        coffee.report()
    elif user_choice == 'off':
        machine_working = False

    elif user_choice != "report" or user_choice != "off":
        coffee_cost = coffee.get_coffee_prize(user_choice)
        if user_choice == 'espresso':
            if coffee.compare_ingredients(user_choice):
                coffee.reduce_machine_resources(coffee)
                change = coffee.calculate_change(user_choice)
                if change < 0:
                    print("Not enough money!")
                else:
                    print(f"Here is your {user_choice}. Enjoy!")
                    print(f"And here is your change: {change}$")
        if user_choice == 'latte':
            if coffee.compare_ingredients(user_choice):
                coffee.reduce_machine_resources(coffee)
                change = coffee.calculate_change(user_choice)
                if change < 0:
                    print("Not enough money!")
                else:
                    print(f"Here is your {user_choice}. Enjoy!")
                    print(f"And here is your change: {change}$")
        if user_choice == 'cappuccino':
            if coffee.compare_ingredients(user_choice):
                coffee.reduce_machine_resources(coffee)
                change = coffee.calculate_change(user_choice)
                if change < 0:
                    print("Not enough money!")
                else:
                    print(f"Here is your {user_choice}. Enjoy!")
                    print(f"And here is your change: {change}$")
    else:
        print("Wrong choice!")


