# Funkcje, while loop oraz indentation
# wedlug oficjalnej dokumentacji Python powinno sie uzywac 4 spacji zamiast tabulatora
# w IDE mozna ustawic ze tabulator bedzie dzialal jako 4 spacje
# for loops sa dobre do iteracji kiedy na kazdym elemencie musimy cos zrobic
# while loops korzystamy wtedy kiedy potrzebujemy spelniac jakis warunek az sie spelni
# nie wiemy wtedy ile tych iteracji bedzie

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     move()
#     if wall_in_front():
#         jump()
#     else:
#         move()

# zmodyfikowana wersja funkcji jump() z kursu dla roznych wysokosci przeszkod dla robota do przeskoczenia
# nie moze byc if poniewaz wtedy wykona sie tylko raz i blok sie wykona dalej i bedzie blad
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

# projekt
# tutaj istnieje mozliwosc ze wpadniemy w nieskonczona petle
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()

# wersja kolejna
# w tej wersji najpierw wykona sie pierwsza petla az dojdziemy do sciany
# potem bedzie sie wykonywac kolejna petal az dojdziemy do celu
# while front_is_clear():
#     move()
# turn_left()
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()
