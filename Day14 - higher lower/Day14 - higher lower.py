# NA FORKLIT JEST ROZWIAZANIE Z KURSU
import art
from game_data import data
import random
import os

compare = random.choice(data)
player_score = 0
playing = True


def check_more_followers(followers_a, followers_b):
    if followers_a > followers_b:
        return compare
    else:
        return against


def check_double(entry_a, entry_b):
    if entry_a == entry_b:
        entry_b = random.choice(data)
        return entry_b
    else:
        return entry_b


# sprawdza odpowiedz
# nie wiem czy nie lepiej by bylo w normalnej petli to napisac ale tak wyglada bardziej elegancko
def check_answer(answer, followers_a, followers_b):
    if answer == 'a' and followers_a > followers_b:
        return True
    elif answer == 'b' and followers_a < followers_b:
        return True


print(art.logo)

while playing:

    print("Compare A:")
    print(f"Name: {compare['name']}\nDescription: {compare['description']}\nCountry: {compare['country']}")
    print(art.vs)

    against = random.choice(data)
    against = check_double(compare, against)
    print("Against B:")
    print(f"Name: {against['name']}\nDescription: {against['description']}\nCountry: {against['country']}")

    compare_followers = compare['follower_count']
    against_followers = against['follower_count']

    question = input("\n\nWho has more followers? A or B? ").lower()

    # sprawdzanie odpowiedzi i jesli nic nie wychodzi z funkcji to jest else i wtedy False
    if check_answer(question, compare_followers, against_followers):
        player_score += 1
    else:
        playing = False

    # sprawdza ktory ma wiecej followersow jesli odpowiedz byla prawidlowa i przypisuje go do pierwszej zmiennej
    compare = check_more_followers(compare_followers, against_followers)
    os.system('cls')

    if not playing:
        print(f"Wrong! Your score is {player_score}")
    else:
        print("You are correct!")
        print(f"Your score is: {player_score}")

