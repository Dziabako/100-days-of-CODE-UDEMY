from turtle import Turtle, Screen
import random

screen = Screen()
# okreslanie wielkosci okna (lepiej uzywac argumentow nazwanych bo wiadomo co i jak wtedy)
screen.setup(width=500, height=400)
# input w postaci wyskakujacego okna (zwraca string podobnie jak funkcja input)
user_bet = screen.textinput(title="Make your bet!", prompt="Enter a color of turtle which will win the race!")


def move_to_start(turtles):
    x_start = -230
    y_start = -100
    for turtle in turtles:
        turtle.penup()
        turtle.goto(x_start, y_start)
        y_start += 50


def racing(turtle):
    turtle.forward(random.randint(0, 10))


# Tworzenie obiektow z kursu
# for t in range(0, 5):
#     tim = Turtle(shape='turtle')
#     tim.color(random.choice('colors'))
#     tim.penup()
#     tim.goto(x_pos, y_pos_list[t.index]


tim_red = Turtle(shape='turtle')
tim_yellow = Turtle(shape='turtle')
tim_blue = Turtle(shape='turtle')
tim_green = Turtle(shape='turtle')
tim_purple = Turtle(shape='turtle')

tim_red.color('red')
tim_yellow.color('yellow')
tim_blue.color('blue')
tim_green.color('green')
tim_purple.color('purple')

racing_turtles = [tim_red, tim_yellow, tim_blue, tim_green, tim_purple]
move_to_start(racing_turtles)

is_racing = True

while is_racing:

    for tim in racing_turtles:
        if tim.xcor() > 230:
            winner = tim.pencolor()
            if winner == user_bet:
                print("That's the winner!")
                is_racing = False
            else:
                print(f"Nope! The winner is {winner}")
                is_racing = False
        racing(tim)


screen.exitonclick()
