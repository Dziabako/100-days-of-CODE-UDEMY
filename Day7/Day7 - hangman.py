def zad1():
    import random
    word_list = ['ardvark', 'baboon', 'camel']
    chosen_word = random.choice(word_list)
    user_choice = input("Guess a letter: ").lower()

    for char in chosen_word:
        if char == user_choice:
            print("Right!")
        else:
            print("Wrong!")


def zad2():
    import random
    word_list = ['ardvark', 'baboon', 'camel']
    chosen_word = random.choice(word_list)
    print(f'Pssst, the solution is {chosen_word}.')

    user_choice = input("Guess a letter: ").lower()

    # zamiast tego moze byc string i wtedy latwiej kreski zrobic, lecz podmiana bedzie wtedy trudniejsza
    display = []
    for n in range(len(chosen_word)):
        display.append("_")
    print(display)

    display = []
    for n in range(len(chosen_word)):
        display.append("_")
        if chosen_word[n] == user_choice:
            display[n] = user_choice
    print(display)

    for n in range(len(chosen_word)):
        if chosen_word[n] == user_choice:
            display[n] = user_choice

    print(display)


def zad3():
    import random
    word_list = ['ardvark', 'baboon', 'camel']
    chosen_word = random.choice(word_list)
    word_lenght = len(chosen_word)
    print(f'Pssst, the solution is {chosen_word}.')

    display = []
    for n in range(len(chosen_word)):
        display.append("_")
    print(display)

    while display != list(chosen_word):
        user_choice = input("Guess a letter: ").lower()
        for n in range(word_lenght):
            if chosen_word[n] == user_choice:
                display[n] = user_choice
        print(display)
    else:
        print("You win")

    # rozwiazanie z kusu
    # end_of_game = False
    # while not end_of_game:
    #     user_choice = input("Guess a letter: ").lower()
    #     for n in range(word_lenght):
    #         if chosen_word[n] == user_choice:
    #             display[n] = user_choice
    #     print(display)
    #
    # if "_" not in display:
    #     end_of_game = True


def zad4and5():
    # rozwiazanie w kursie jest inne niz moje
    # do wgladu w kursie DAY 7 CHALLENGE 4
    import random
    import Day7_hangman_words
    from Day7_hangman_pics import HANGMAN

    chosen_word = random.choice(Day7_hangman_words.word_list)
    word_lenght = len(chosen_word)
    print(f'Pssst, the solution is {chosen_word}.')

    lives = len(HANGMAN)
    used = []

    display = []
    for n in range(word_lenght):
        display.append("_")
    print(display)

    while list(chosen_word) != display and lives > 0:
        user_guess = input("Guess a letter: ")
        if user_guess in chosen_word:
            for i in range(word_lenght):
                if chosen_word[i] == user_guess:
                    display[i] = user_guess
        elif user_guess not in chosen_word and user_guess not in used:
            used.append(user_guess)
            print("There is no such letter in the secret word")
            print(HANGMAN[-lives])
            lives -= 1
        else:
            print("You already used that letter!")
        print(display)
        print(f'You still have {lives} lives left')
        print(f'You already used this letters: {used}')

    if display == list(chosen_word):
        print("Thats it! You Have Won!\nThe word is:")
        print(f"{''.join(display)}")
    else:
        print("You've run out of lives! Game Over!")


zad4and5()
