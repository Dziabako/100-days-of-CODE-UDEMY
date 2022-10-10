# # otwierane pliki nalezy przypisac do zmiennej by moc na nich operowac
# # plik znajduje sie w tym samym folderze co plik pythona
# # mozna tez podac cala sciezke znajdujaca sie w innym folderze
# file = open("my_file.txt")
#
# # zwracanie zawartosci pliku jako string
# contents = file.read()
# print(contents)
#
# # zamykanie pliku (zamykay by zwolnic zajeta pamiec przez otwarty plik)
# file.close()
#
# # inna metoda na otwieranie pliku i jego automatyczne zamykanie
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#
# # dodawanie lini tekstu do pliku
# # wazne jest zeby zmienic tryb bo domyslnie jest uruchamiany jako tylko do odczytu
# # "w" - nadpisuje istniejacy plik
# # "a" - dodaje do istniejacego pliku
# with open("my_file.txt", "w") as file:
#     file.write("\nBla Bla")
#
# # jezeli plik nie istnieje to przy uzyciu tej metody stowrzy sie on automatycznie
# with open("new_file.txt", "w") as file:
#     file.write("Bla Bla")

# ABSOLUTE PATH - pelna sciezka do pliku zaczynajaca sie od dysku (ROOT) [/folder/folder/folder/plik]

# RELATIVE PATH - sciezka do pliku zaczynajaca sie od folderu roboczego [./plik] [./folder/plik]
# ./ oznacza ze zaczynamy z folderu roboczego
# jezeli chcemy isc do folderu nadrzednego uzywamy sciezki - ../plik

# sciezke zapisujemy jako raw string inaczej wyskakuje blad
# w Windows nalezy podac na poczatku na ktorym dysku znajduje sie plik
path = r"C:\Users\dziab\OneDrive\Pulpit\new_file.txt"
with open(path) as file:
    print(file.read())

# sciezka relatywna
path = r"..\..\..\Pulpit\new_file.txt"
with open(path) as file:
    print(file.read())
