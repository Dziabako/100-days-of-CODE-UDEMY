# local scope - jezeli zmienna jest stworzona w danym srodowisku (funkcja) jest ona dostepna tylko w niej

# global scope - jest to zmienna globalna dostepna wszedzie, jest deklarowana przed funkcja
# mozna ja normalnie uzyc wewnatrz funkcji
# w celu zmiany wartosci zmiennej globalnej (zdefiniowanej poza funkcja) nalezy w funcji uzyc: global zmienna
# w ten sposob mozemy ja modyfikowac
# lepiej nie uzywac tego zbyt czesto poniewaz moze to powodowac bledy ktorych nie chcemy
# najlepiej jest tego unikac
# jezeli chcemy tego unikac mozemy uzyc return w funkcji w celu zmiany wartosci zmiennej globalnej

# STALE GLOBALNE to zmienne ktore tworzymy i nie chcemy ich zmieniac w przyszlosci
# takie zapisujemy uzywajac duzych liter
# ZMIENNA = warotsc

# namespace - koncept mowiacy o tym ze zmienna ma nazwa i jest dostepna ze wzgledu na jej miejsce w programie
# nalezy byc swiadomym gdzie dana zmienna, funkcja itp jest stworzona i gdzie jest uzywana
# nie ma czegos jak BLOCK SCOPE
# jezeli stworzymy cos w bloku kodu nie liczy sie to jako osobny scope

import random

HARD_LIFES = 5
EASY_LIFES = 10
number = random.randint(1, 101)
print(f"Control: {number}")
tries = None

game_mode = input("Do you want to play EASY mode or HARD mode?: ").lower()
if game_mode == 'hard':
    print("You have choose HARD mode! You have only 5 tries!\n")
    tries = HARD_LIFES
elif game_mode == 'easy':
    print("You have choose EASY mode! You have 10 tries!\n")
    tries = EASY_LIFES
else:
    print("Wrong choice! Try again!")

guess = int(input("Guess a number from 1 to 100: \n"))

while guess != number and tries > 0:
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    print(f"You still have {tries} tries left!")
    tries -= 1
    guess = int(input("Guess a number from 1 to 100: \n"))

if guess == number and tries > 0:
    print("Congrats! You Win!")
else:
    print("You lost!")
    print(f"The number was: {number}")
