# random.randint(a, b) - zwraca losowa liczbe z podanego przedzialu lacznie z podanymi liczbami
# random.randrange(start(opt), stop, step(opt)) - to samo co wyzej tylko ze mamy step i nie jest liczona ostatnia liczba
# przy randint potrzeba obu argumentow a przy randrange wystarczy jeden
# randrange moze byc lepszy do indeksowania
# random.random() - zwraca losowa liczbe przecinkowa pomiedzy 0 i 1
# random.random * random.randint(a, b) - zwiekszenie losowe liczby przecinkowej

# moduly mozemy tworzyc samemu
# lecz zeby je wykorzystac musza byc one w tym samym folderze co plik do ktorego go importujemy

# tutaj jest wykorzystana python package, ktore importujemy w taki sposob
# sa one dostepne w kazdym folderze z plikami, byle byly w glonym folderze
# python package to jest osobny folder sam w sobie
# __init__.py przez to python traktuje ten folder jako pacze z modulami
# import ecommerce.shipping
# print(ecommerce.shipping.cal_shipping())
# from ecommerce import shipping
# print(shipping.cal_shipping())

def zad1():
    import random

    throw = random.randint(0, 1)
    if throw == 0:
        print("Tails!")
    else:
        print("Heads!")


def zad2():
    import random

    name_string = input("Give me everybody's names, separated by coma. ")
    names = name_string.split(", ")

    random_index = random.randrange(len(names))
    print(f"{names[random_index]} is going to buy the meal today!")


def zad3():
    row1 = ["O", "O", "O"]
    row2 = ["O", "O", "O"]
    row3 = ["O", "O", "O"]
    mapa = [row1, row2, row3]

    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do yo want to put the treasure? ")

    pos = position.split(" ")
    mapa[int(pos[0]) - 1][int(pos[1]) - 1] = "X"
    print(f"{row1}\n{row2}\n{row3}")


def zad3_2():
    # rozwiazanie z kursu
    row1 = ["O", "O", "O"]
    row2 = ["O", "O", "O"]
    row3 = ["O", "O", "O"]
    mapa = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do yo want to put the teasure? ")

    horizontal = int(position[0])
    vertical = int(position[0])

    selected_row = mapa[vertical - 1]
    selected_row[horizontal - 1] = 'X'

    print(mapa)


def project():
    import random
    rps = ["rock", "paper", "scissors"]
    com_choice = random.choice(rps)
    user_choice = input("What do you choose? Rock, paper or scissors\n").lower()

    if user_choice == 'rock':
        print(com_choice)
        if com_choice == 'paper':
            print('Computer Wins!')
        elif user_choice == com_choice:
            print("It's a tie!")
        else:
            print('You win!')
    elif user_choice == 'paper':
        print(com_choice)
        if com_choice == 'scissors':
            print('Computer Wins!')
        elif user_choice == com_choice:
            print("It's a tie!")
        else:
            print('You win!')
    elif user_choice == 'scissors':
        print(com_choice)
        if com_choice == 'rock':
            print('Computer Wins!')
        elif user_choice == com_choice:
            print("It's a tie!")
        else:
            print('You win!')
    else:
        print("Wrong Choice!")


project()

