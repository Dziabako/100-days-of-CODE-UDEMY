def zad1():
    number = int(input("Which number do you want to check? "))
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


def zad2():
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in kg: "))
    bmi = round(weight / (height ** 2), 1)
    if bmi < 18.5:
        print("You are underweight!")
    elif bmi < 25:
        print("You have normal weight")
    elif bmi < 30:
        print("You are overweight!")
    elif bmi < 35:
        print("You are obese!")
    else:
        print("You are clinically obese!")


def zad3():
    # jezeli rok jest podzielny przez 100 to nie jest to rok przestepny
    # chyba ze jest dodatkowo podzielny przez 400 to jest przestepny
    # inaczej uruchamia się ten fragment z else

    year = int(input("Which year do you want to check? "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year!")
            else:
                print(f"{year} is NOT a leap year!")
        else:
            print(f"{year} is a leap year!")
    else:
        print(f"{year} is NOT a leap year!")


# jezeli uzywamy if/elif tylko jeden warunek zostanie spelniony
# lecz jezeli uzyjemy kilku warunkow if to wszystki one moga zostac spelnione i wykonane
# lub tylko te ktorych warunek zostal spelniony
# jest to tak jakby kolejny blok if/elif/else


def zad4():
    print("Welcome to Python Pizza Deliveries!")
    size = input('What size pizza do you want? S, M or L? ').upper()
    add_pepperoni = input("Do you want Pepperoni? Y or N? ").upper()
    extra_cheese = input("Do you want extra cheese? Y or N? ").upper()

    bill = 0

    if size == "S":
        bill += 15
        if add_pepperoni == "Y":
            bill += 2
        if extra_cheese == "Y":
            bill += 1
    elif size == "M":
        bill += 20
        if add_pepperoni == "Y":
            bill += 3
        if extra_cheese == "Y":
            bill += 1
    elif size == "L":
        bill += 25
        if add_pepperoni == "Y":
            bill += 3
        if extra_cheese == "Y":
            bill += 1
    else:
        print("Wrong Entry!")
    print(f"Your final bill is {bill}$ for the pizza")


def zad4_2():
    # rozwiazanie z kursu
    print("Welcome to Python Pizza Deliveries!")
    size = input('What size pizza do you want? S, M or L? ').upper()
    add_pepperoni = input("Do you want Pepperoni? Y or N? ").upper()
    extra_cheese = input("Do you want extra cheese? Y or N? ").upper()
    bill = 0
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    elif size == "L":
        bill += 25

    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is {bill}$ for the pizza")


def zad5():
    # w kursie jest to bez petli for tylko recznie wszystko jest wypisane
    print("Welcome to Love Calculator!")
    name1 = input("What is your name?\n").lower()
    name2 = input("What is their name?\n").lower()

    # combined_name bylo z kursu
    combined_name = name1 + name2
    true = "true"
    love = "love"
    true_count = 0
    love_count = 0

    # string.count(str) zwraca ilosc wystepowania danegogo str w innym str
    for i in range(4):
        true_count += combined_name.count(true[i])
        love_count += combined_name.count(love[i])

    total = str(true_count) + str(love_count)
    love_score = int(total)

    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif 40 < love_score < 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}.")


def treasure_island():
    print("Welcome to the Treasure Island!")
    print("Your mission is to find the treasure!")

    choice = input("You standind at the road. Where do you want to go? Left or Right?\n").lower()
    if choice == 'right':
        print("You fell into a hole and died! Game Over!")
    else:
        choice = input("You arrived at the port. Do you want to 'wait' for the boat or 'swim' by yourself?\n").lower()
        if choice == 'wait':
            print("You arrived safely on the island")
            print("Now you are in the house in the woods with doors. Yellow, BLue, Red and Other")
            choice = input("What do u choose?\n").lower()
            if choice == 'red':
                print("You burned alive! Game Over!")
            elif choice == 'yellow':
                print("This is IT! You Have Won!")
            elif choice == 'blue':
                print('You have been eaten by beasts! Game Over!')
            else:
                print("Not there! Game Over!")
        else:
            print("You died in trout stomach! Game Over!")


treasure_island()

