class CoffeeMaker(object):
    def __int__(self, choice):
        self.choice = choice
        self.menu = {
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
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0,
        }
        self.coins = {
            "quarter": 0.25,
            "dimes": 0.1,
            "nickles": 0.05,
            "pennies": 0.01,
        }

    def report(self):
        print(f"""
        Water: {self.resources["water"]}
        Milk: {self.resources["milk"]}
        Coffee: {self.resources["milk"]}
        Money: {self.resources["money"]}""")

    def get_coffee(self, choice):
        coffee = {}
        coffee["water"] += self.menu[choice]["ingredients"]["water"]
        coffee["coffee"] += self.menu[choice]["ingredients"]["coffee"]
        if "milk" in self.menu[choice]["ingredients"]:
            coffee["milk"] += self.menu[choice]["ingredients"]["milk"]
        return coffee

    def get_coffee_prize(self, choice):
        return self.menu[choice]["cost"]

    def reduce_machine_resources(self, coffee):
        for x in coffee:
            if x in self.resources:
                self.resources[x] -= coffee[x]
        return self.resources

    def compare_ingredients(self, coffee):
        for i in coffee:
            if coffee[i] > self.resources[i]:
                print(f"Sorry! We have run out of {i}")
                return False
        else:
            return True

    def calculate_coin_value(self, q, d, n, p):
        quarter_value = q * self.coins["quarter"]
        dimes_value = d * self.coins["dimes"]
        nickles_value = n * self.coins["nickles"]
        pennies_value = p * self.coins["pennies"]
        return sum([quarter_value, dimes_value, nickles_value, pennies_value])

    def calculate_change(self, choice):
        user_quarter = int(input("How many quarters? "))
        user_dimes = int(input("How many dimes? "))
        user_nickles = int(input("How many nickles? "))
        user_pennies = int(input("How many pennies? "))

        coffee_price = self.get_coffee_prize(choice)
        coins_value = self.calculate_coin_value(user_quarter, user_dimes, user_nickles, user_pennies)

        return round(coins_value - coffee_price, 2)
