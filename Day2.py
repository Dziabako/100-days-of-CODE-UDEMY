# duze liczby w Python mozna zapisac w taki sposob
# 123_456_789
# type() - sprawdza jakim rodzajem zmiennej jest dana zmienna

def zad1():
    two_digit_number = input("Type a two digit number: ")
    first_number = two_digit_number[0]
    second_number = two_digit_number[1]
    print(f"{first_number} + {second_number} = {int(first_number) + int(second_number)}")


def zad2():
    height = input("Enter your height in m: ")
    weight = input("Enter your weight in kg: ")
    bmi = int(weight) / (float(height) ** 2)
    # round zaokrągla liczbe przecinkową do danej ilości miejsc po przecinku
    # bez podania ilości miejsc po przecinku zaokragla do pelnej liczby
    print(f"Your BMI is: {round(bmi, 2)}")
    print("Your BMI is: %.2f" % bmi)
    # w tym wypadku musi byc ':', poniewaz wyskoczy blad ze float lub int nie ma formatu 2f
    print("Your BMI is: {:.2f}".format(bmi))


def zad3():
    age = int(input("What is your current age? "))
    left_age = 90 - age
    print(f'You have {left_age * 365} days, {left_age * 52} weeks and {left_age * 12} months')


def tip_calculator():
    print("welcome to the tip calculator.")
    bill = input('What was the total bill? $')
    tip = input('What percentage tip you want to give? 10, 12 or 15? ')
    people = input('How many people to split the bill? ')
    pay = (float(bill) + (float(bill) * (int(tip) / 100))) / int(people)
    print(f'Each person should pay {round(pay, 2)}')
    print(f'Each person should pay %.2f' % pay)


tip_calculator()

