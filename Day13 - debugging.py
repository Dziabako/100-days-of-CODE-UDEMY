# ###########DEBUGGING#####################

# Describe Problem
# funkcja sie nie wykonuje poniewaz range jest do 20 czyli bedzie dzialala tylko do 19
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
# my_function()

# # Reproduce the Bug
# BUG to INDEX ERROR
# wyskakuje poniewaz jest uzyty randint w zakresie od 1 do 6
# czyli index bedzie losowo czasami wynosil 6 co jest juz poza zakresem listy
# lista ma index od 0 do 5
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# przy wpisaniu 1994 nic nie wyskakuje poniewaz wedlug zalozen funkcji 1994 nie jest nigdzie brane pod uwage
# powinno byc chociaz w jednym if <= lub >=
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# bledy wyskakuja ze wzgledu na zle wciecia kodu oraz zly typ zmiennej
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# blad wyskakiwal poniewaz w input word_per_pages jest '==' zamiast '='
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Pages = {pages}")
# print(f"Words = {word_per_page}")
# print(total_words)

# #Use a Debugger
# funkcja zle sie wykonywala poniewaz b_list.append(new_item) znajdowalo sie poza petla for
# dlatego tez tylko ostatni element z petli dodawal sie do listy
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1,2,3,5,8,13])

