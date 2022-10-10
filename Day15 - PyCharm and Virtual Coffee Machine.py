# przy otwartych dwoch kartach z projektami mozna je wyswietlic na podzielonym ekarnie
# klikamy wtedy prawym klawiszem myszu na karte ktora chcemy wyswietlic na podzilonym ekranie

# Python style guide - PEP 8 - DO SPRAWDZENIA

# VCS -> local history -> show history - historia stworzonych projektow / kodow
# z lewej 'structure' pokazuje wsyzstkie zmienne i funkcje w danym projekcie
# prawy klawisz na zmiennej lub funkcji -> refractor -> rename
# w ten sposob mozemy na raz zmienic nazwe danej funkcji / zmiennej i wszystkich jej wywolan

# mamy do tego możliwosc ogladania struktury kazdego projektu pokazujące wszystkie funkcje i zmienne w projekcie

# WIRTUALNA MASZYNA DO KAWY

# mozna opisac kroki poza ekranem do pisania kodu korzystając z zakładki T O D O umieszczonej na dole
# nastepnie mozemy uzywac konsoli na dole by przenosic sie do kazdego zadania osobno

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

COINS = {
    "quarter": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01,
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def ingredients_dict(choice):
    coffee_ingredients = {"water": MENU[choice]["ingredients"]["water"]}
    if 'milk' in MENU[choice]["ingredients"]:
        coffee_ingredients["milk"] = MENU[choice]["ingredients"]["milk"]
    coffee_ingredients["coffee"] = MENU[choice]["ingredients"]["coffee"]
    return coffee_ingredients


def get_coffee_prize(choice):
    coffee_cost = 0
    coffee_cost += MENU[choice]["cost"]
    return coffee_cost


def reduce_machine_resources(coffee, ingredients):
    for x in coffee:
        if x in ingredients:
            ingredients[x] -= coffee[x]
    return ingredients


def compare_ingredients(coffee_choice, machine_ingredients):
    for i in coffee_choice:
        if coffee_choice[i] > machine_ingredients[i]:
            print(f"Sorry! We have run out of {i}")
            return False
    else:
        return True


def calculate_coin_value(q, d, n, p):
    quarter_value = q * COINS["quarter"]
    dimes_value = d * COINS["dimes"]
    nickles_value = n * COINS["nickles"]
    pennies_value = p * COINS["pennies"]
    return sum([quarter_value, dimes_value, nickles_value, pennies_value])


def calculate_change():
    user_quarter = int(input("How many quarters? "))
    user_dimes = int(input("How many dimes? "))
    user_nickles = int(input("How many nickles? "))
    user_pennies = int(input("How many pennies? "))

    coffee_price = get_coffee_prize(user_choice)
    coins_value = calculate_coin_value(user_quarter, user_dimes, user_nickles, user_pennies)

    return round(coins_value - coffee_price, 2)


machine_working = True


while machine_working:

    user_choice = input("What would you like? (espresso/latte/cappuccino: ").lower()
    chosen_coffee = None
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        chosen_coffee = ingredients_dict(user_choice)

    if user_choice == 'report':
        print(f"""
        Water: {resources["water"]}
        Milk: {resources["milk"]}
        Coffee: {resources["milk"]}
        Money: {resources["money"]}""")
    elif user_choice == 'off':
        machine_working = False

    elif user_choice != "report" or user_choice != "off":
        coffee_money = get_coffee_prize(user_choice)
        if user_choice == 'espresso':
            if compare_ingredients(chosen_coffee, resources):
                reduce_machine_resources(chosen_coffee, resources)
                change = calculate_change()
                if change < 0:
                    print("Not enough money!")
                else:
                    print(f"Here is your {user_choice}. Enjoy!")
                    print(f"And here is your change: {change}$")
        elif user_choice == 'latte':
            if compare_ingredients(chosen_coffee, resources):
                reduce_machine_resources(chosen_coffee, resources)
                change = calculate_change()
                if change < 0:
                    print("Not enough money!")
                else:
                    print(f"Here is your {user_choice}. Enjoy!")
                    print(f"And here is your change: {change}$")
        elif user_choice == 'cappuccino':
            if compare_ingredients(chosen_coffee, resources):
                reduce_machine_resources(chosen_coffee, resources)
                change = calculate_change()
                if change < 0:
                    print("Not enough money!")
                else:
                    print(f"Here is your {user_choice}. Enjoy!")
                    print(f"And here is your change: {change}$")
        resources["money"] += coffee_money
    else:
        print("Wrong Choice!")
