# MOJA WERSJA GRY
# PRAWDOPODBNIE NIE JEST POPRAWNA JESLI CHODZI O ZASADY I JEST TROCHE PRZEKOMBINOWANE
# WERSJA Z KURSU ZNAJDUJE SIE W ZAKLADCE W GOOGLE CHROME 'PYTHON COURSE'

import random
import os

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(hand):
    return hand.append(random.choice(CARDS))


def check_score(hand):
    score = 0
    for c in hand:
        score += c
    return score


def another_card(player_hand):
    deal_card(player_hand)
    player_score = check_score(player_hand)
    if player_score > 21:
        CARDS[0] = 1
        player_score = check_score(player_hand)
    print(f"Player cards: {player_hand}")
    return player_score


def check_win(points_player, points_dealer):
    if points_player == 21 and points_dealer == 21:
        print(f"Player: {points_player}\nDealer: {points_dealer}\nDealer have WON!")
    elif points_player > 21:
        print(f"Player: {points_player}\nBUST!\nDealer have WON!")
    elif points_dealer > 21:
        print(f"Dealer: {points_dealer}\nBUST!\nPlayer have WON!")
    elif points_player > points_dealer:
        print(f"Player: {points_player}\nDealer: {points_dealer}\nPlayer have WON!")
    elif points_player < points_dealer:
        print(f"Player: {points_player}\nDealer: {points_dealer}\nDealer have WON!")


def blackjack():
    player = []
    dealer = []
    # wydawanie kart dla gracza i krupiera
    for n in range(2):
        deal_card(player)
        deal_card(dealer)

    # wyswietlanie uzyskanych kart
    print(f"Dealer cards: {dealer[0]}")
    print(f"Player cards: {player}")

    # tura gracza i dodawanie kolejnych kart jesli chce
    draw_card = True
    while draw_card:
        ask = input("Do you want to draw another card? Y / N? ").lower()
        if ask == 'y':
            player_points = another_card(player)
        else:
            player_points = check_score(player)
            draw_card = False

    # tura komputera i dodawanie kolejnych kart jesli spelnione sa warunki
    dealer_draw = True
    while dealer_draw:
        dealer_points = check_score(dealer)
        if dealer_points > 21:
            CARDS[0] = 1
        dealer_points = check_score(dealer)
        if dealer_points < 17:
            deal_card(dealer)
        else:
            dealer_draw = False

    # wyswietlanie ostatecznej reki obu graczy i pokazywanie wynikow
    # nie wiem czemu wyskakuje tutaj ten komunikat ze powinno byc przydzielone wczesniej
    print(f"Dealer cards: {dealer}")
    print(f"Player cards: {player}")
    check_win(player_points, dealer_points)

    # kontynuowanie gry lub jej koniec
    is_continue = True
    if is_continue:
        again = input("Do you wanna play again? Y / N? ").lower()
        if again == 'y':
            os.system('cls')
            blackjack()
        elif again == 'n':
            print("Good Bye!")
        else:
            print("Wrong choice! Try again!")


blackjack()
