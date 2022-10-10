# CTRL + / - automatyczne komentowanie linii kodu lub calego bloku
# CTRL + z - cofanie zmian
# Syntax Error to zwyczajny bład powstający przy literówce
# Indentation Error to bład spacji w kodzie, czyli zle pozyconowany kod
def day1_1():
    print("Day 1 - Python print function")
    print("The function is declared like this:")
    print("print('what to print')")


def day1_2():
    print("Day 1 - String Manipulation")
    print("String Concatenation is done with the '+' sign")
    print("e.g. print('Hello ' + 'World')")
    print("New line can be created with backslash and n.")


def day1_3():
    # fajne wykorzystanie funkcji input
    # najpierw wykona sie input a potem print z pozykanymi danymi
    # print("Hello " + input("What is your name? "))
    print(len(input("What is your name: ")))


def day1_4():
    a = input("a: ")
    b = input("b: ")

    x = a
    a = b
    b = x

    print("a = " + a)
    print("b = " + b)


def day1_project():
    print("Welcome to the Band Name Generator.")
    city = input("What's the name of the city ou grew up in?\n")
    pet = input("What's yours pet's name?\n")
    print(f"Your band name could be: {city} {pet}")


day1_project()

