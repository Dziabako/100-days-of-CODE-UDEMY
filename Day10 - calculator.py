# .title() zwraca strig z pierwsza litera duza
# return w funkcji konczy wykonywanie funkcji wiec to co jest po return nie wykona sie
# nie broni to jednak przed dawaniem kilku wartosci return
# mozna tez dac pusty return

# Docstring
# tworzenie niewielkiej dokumentacji w czasie kodowania lub w naszych blokach kodu
# docstring idzie jako pierwsza linia po deklaracji funkcji
# """ docstring (opis funkcji) """

# return - zwraca wartosc
# print - wyswietla wartosc nic nie zwracajac, nie mozna na tym dalej nic zrobic

def format_name(f_name, l_name):
    f_name.title()
    l_name.title()
    return f"{f_name} {l_name}"


def zad1():
    def is_leap(y):
        """ Sprawdzanie czy rok jest przestepny """
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    # jezeli wprowadzone dane sprawiaja ze nie jest zwracana zadna wartosc to przy wywolaniu bedzie None
    def days_in_month(y, m):
        if m > 12 or m < 1:
            return "Invalid month"
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(y) and m == 2:
            return 29
        return month_days[m - 1]

    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)


def calculator():
    import os

    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2

    # podajemy bez nawiasow by nie podawac danych wejsciowych przez co nie ma bledu
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    # wsyzstko jest wpisane w funkcje by moglo byc potem jeszcze raz wywolane
    # jest to tak zwana rekurencja
    # czyli funkcja na koniec wywoluje sama siebie
    def calc():
        num1 = float(input("What's the first number?: "))
        is_continue = True

        print("Operations:")
        for k in operations.keys():
            print(k)

        while is_continue:
            operation_symbol = input("Pick an operation from the line above: ")
            num2 = float(input("What's the next number?: "))

            function = operations[operation_symbol]
            result = function(num1, num2)

            print(f"{num1} {operation_symbol} {num2} = {result}")

            continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start again: ")

            if continue_calc == "y":
                num1 = result

            elif continue_calc == "n":
                os.system('cls')
                is_continue = False
                # w tym miejscu jesli damy 'n' funkcja sie wywola jeszcze raz
                # wszystki sie wtedy resetuje i wraca do poczatkowych wartosci
                calc()

            else:
                print("Wrong choice! Try again!\n")

    # zeby zadzialalo musimy ja napierw normalnie wywolac
    # trzeba uwazac by nie stworzyc infinite loop
    calc()

    # PONIZEJ JEST MOJE ROZWIAZANIE KTORE JEST DLUGIE

    # MOJE ROZWIAZANIE KTORE NIESTETY JEST ZA DLUGIE
    # num1 = int(input("What's the first number?: "))
    # num2 = int(input("What's the second number?: "))
    #
    # print("Operations:")
    # for k in operations.keys():
    #     print(k)
    #
    # operation_symbol = input("Pick an operation from the line above: ")
    #
    # function = operations[operation_symbol]
    # result = function(num1, num2)
    #
    # print(f"{num1} {operation_symbol} {num2} = {result}")
    #
    # is_continue = True
    # new_result = result
    #
    # while is_continue:
    #     continue_calculation = input(f"Type 'y' to continue calculating with {new_result}, or type 'n' to exit:  ")
    #
    #     if continue_calculation == "y":
    #         number = new_result
    #         operation_symbol = input("Pick an operation from the line above: ")
    #         new_num = int(input("What's the next number?: "))
    #         new_function = operations[operation_symbol]
    #         new_result = new_function(number, new_num)
    #
    #         print(f"{number} {operation_symbol} {new_num} = {new_result}")
    #
    #     elif continue_calculation == "n":
    #         os.system('cls')
    #         is_continue = False
    #
    #     else:
    #         print("Wrong choice! Try again!\n")


calculator()
