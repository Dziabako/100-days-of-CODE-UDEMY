# *args to krotka (lista) z wartosciami ktore mozna w dowolnej ilosci dodac do funkcji
# moze byc inna nazwa
# wazne by przed ta nazwa byla '*' co oznacza ze mamy doczynienia z wieksza iloscia wartosci w funkcji
# sa to argumenty bez nazwy

# **kwargs sa to argumenty w funkcji ktore maja nazwe
# mozemy je rowniez wpisywac w dowolnej ilosci lecz musza byc one nazwane
# tym przypadku mamy doczynienia ze slownikiem
# jezeli do funkcji wrzucamy liste lub slownik jako argument nalezy nzawy obu poprzedzic '*' lub '**'
# w ten sposob zostana one odczytane odpwiednio
# uzywajac *args oraz **kwargs mozemy tworzyc funkcje ktore sa bardziej elastyczne pod wzgledem przyjmowanych argumentow

# argumenty pozycyjne sa odczytywane wedlug swojej pozycji
# keyword argument sa to argumenty nazwane, ktore wykonuja sie wedlug podanej nazwy zmiennej a nie wedlug kolejnosci

def zad1():
    import math
    # round nie zawsze zaokragli do gory
    # math.ceil zawsze zaogragla do gory nawet jesli powinno byc w dol

    def paint_calculator(height, width, coverage):
        number_of_cans = math.ceil((height * width) / coverage)
        print(f"Numbers of cans needed to paint this wall is: {number_of_cans}")

    h = int(input("Height of wall: "))
    w = int(input("Width of wall: "))
    c = 5

    paint_calculator(h, w, c)


def zad2():
    def prime_check(n):
        prime_num = True
        for num in range(2, n):
            # nie ma else bo jak sie zmieni raz na False to nie chcemy by znowu bylo True
            if n % num == 0:
                prime_num = False

        if prime_num:
            print("It is a prime number")
        else:
            print("It is not a prime number")

    number = int(input("Check this number: "))
    prime_check(number)


def project():
    # moja wersja nie wedlug tresci zadania
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    # w obu przypadkach mozna bylo pominac zamiane na liste i potem jej laczenie w str
    # wtedy by wygladalo tak samo tylko ze bez list
    # jest to pokazane w kolejnej funkcji project2()
    def encrypt(t, s):
        t = list(t)
        new_t = []
        for n in t:
            new_t.append(alphabet[alphabet.index(n) + int(s)])
        new_t = ''.join(new_t)
        print(f"The encoded text is {new_t}")

    def decrypt(t, s):
        t = list(t)
        old_t = []
        for n in t:
            old_t.append(alphabet[alphabet.index(n) - int(s)])
        old_t = ''.join(old_t)
        print(f"The decoded text is {old_t}")

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    while direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = input("Type the shift number:\n")
        if direction == 'encode':
            encrypt(text, shift)
        elif direction == 'decode':
            decrypt(text, shift)

        again = input("Do you want to go again? Yes / No\n").lower()
        if again == 'yes':
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        else:
            print("Good Bye!")
            break


def project2():
    # DO DODANIA ZAPETLANIE JESLI DOJDZIEMY Z KODOWANIEM DO KONCA ALFABETU
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    def check_shift(shift_len):
        if shift_len > len(alphabet):
            shift_len %= len(alphabet)
            return shift_len
        else:
            return shift_len

    def caesar(d, t, s):
        s = check_shift(s)
        if d == 'encode':
            cipher = ''
            for char in t:
                if char in alphabet:
                    new_pos = alphabet.index(char) + s
                    cipher += alphabet[new_pos]
                else:
                    cipher += char
            print(f"The encoded text is: {cipher}")
        elif d == 'decode':
            old = ''
            for char in t:
                if char in alphabet:
                    old_pos = alphabet.index(char) - s
                    old += alphabet[old_pos]
                else:
                    old += char
            print(f"Decoded text is: {old}")

    # rozwiazanie z kursu
    # def caesar(start_text, shift_ammount, cipher_direction):
    #     end_text = ""
    #     if cipher_direction == 'decode':
    #         shift_ammount *= -1
    #     for letter in start_text:
    #         position = alphabet.index(letter)
    #         new_position = position + shift_ammount
    #         end_text += alphabet[new_position]
    #     print(f"{cipher_direction} text is: {end_text}")

    def questions():
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)

    questions()
    while True:
        question = input("Do you want to continue? Yes or No\n").lower()
        if question == 'yes':
            questions()
        else:
            print("Good Bye!")
            break


project2()
