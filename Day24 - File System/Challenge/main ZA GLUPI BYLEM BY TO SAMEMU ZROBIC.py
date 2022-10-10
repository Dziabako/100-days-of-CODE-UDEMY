PLACEHOLDER = "[name]"

# tworzenie listy gosci z pliku
# na koncu kazdegu elementu jest '\n' poniewaz w pliku kazdy element jest od nowej linii
with open("invited_names.txt") as guests:
    guests = guests.readlines()

# otwieranie poczatkowego listu
with open("starting_letter.txt") as letter:
    letter = letter.read()
    for guest in guests:
        # usuwanie '\n' z kazdego imienia na liscie
        stripped_guest = guest.strip()
        # zamiana [name] na imie z listy
        new_letter = letter.replace(PLACEHOLDER, stripped_guest)
        # tworzenie nowych pojedynczych listow
        with open(rf".\ReadyToSend\letter_for_{stripped_guest}.txt", "w") as invitation:
            invitation.write(new_letter)
