# dodawanie info do slownika
# slownik[nowy_klucz] = nowa wartosc
# slownik mozna wykasowac przez uzycie - istniejacy_slownik = {}
# iteracja przez slownik
# for key in dictionary:
#     print(key, dictionary[key])
# w pliku przypomnienie.py jest iteracja po slowniku w slowniku

def zad1():
    # w taki sposob powinno sie tworzyc slowniki
    # na koncu slownika stawia sie przecinek by w razie czego latwo dodac nowe dane

    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }

    student_grades = {}

    # wystarczy dac wiesze niz dana liczba bo jak wykona sie pierwsze to kolejne juz nie
    for student in student_scores:
        if student_scores[student] > 90:
            student_grades[student] = "Grade - Outstanding!"
        elif student_scores[student] > 80:
            student_grades[student] = "Grade - Exceeds Expectations!"
        elif student_scores[student] > 70:
            student_grades[student] = "Grade - Acceptable!"
        elif student_scores[student] <= 70:
            student_grades[student] = "Grade - Fail!"

    print(student_grades)


def zad2():
    travel_log = [
        {
            "country": 'France',
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "country": 'Germany',
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
    ]

    # moze tez byc zrobione tradycyjna metoda dodawania do pustego slownika
    # slownik[klucz] = wartosc
    def add_new_country(country, visits, cities):
        temp_dict = {
            "country": country,
            "visits": visits,
            "cities": cities
        }

        travel_log.append(temp_dict)

    add_new_country("Denmark", 7, ["Esbjerg, Kopenhagen"])
    print(travel_log)


def secret_auction():
    import os

    # funkcja do resetowania terminalu
    # wystarczy samo os.system('cls') - dla linuxa bedzie 'clear'
    # w run configuration pliku trzeba zaznaczyc 'emulate terminal in output console'
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    bidders = {}
    continue_bidding = True

    # ROZWIAZANIE Z KURSU
    # def find_highest_bidder(bidding_record):
    #     highest_bid = 0
    #     winner = ""
    #     for bidder in bidding_record:
    #         bid_amount = bidding_record[bidder]
    #         if bid_amount > highest_bid:
    #             highest_bid = bid_amount
    #             winner = bidder
    #     print(f"The winner is {winner} with a bid of ${highest_bid}")

    while continue_bidding:
        bidder = input("What is your name?\n")
        bid = int(input("What is your bid: \n$"))
        bidders[bidder] = bid
        question = input("Are there other bidders? Yes / No\n").lower()
        if question == 'yes':
            clear()
        else:
            continue_bidding = False
            clear()
            # find_highest_bid(bidders) - ROZWIAZANIE Z KURSU

    highest_bid = max(bidders.values())
    # inne wykorzystanie funkcji max do szukania klucza z najwieksza wartoscia
    # pierwszy argument to slownik
    # drugi argument musi byc nazwany bo inaczej Python bedzie go czytal jako inny argument czyli liczbe iteracji
    # key jest to argument gdzie nastepuje iteracja danych (kluczy)
    # nastepnie porownywane sa na podstawie zwracanej wartosci i zwracany jest klucz z najwieksza wartoscia
    # przy get nie sa wymagane (), poniewaz w takim przypadku nie trzeba podawać nazwy klucza recznie
    # jest on przez to szukany automatycnzie na podstawie wszystkich wartosci kluczy
    highest_bidder = max(bidders, key=bidders.get)

    print(f"Highest bid is ${highest_bid} made by {highest_bidder}")


secret_auction()
