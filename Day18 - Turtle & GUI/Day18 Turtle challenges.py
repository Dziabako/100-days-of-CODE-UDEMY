import turtle
from turtle import Turtle, Screen
import random

# Challenge 1
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
#
# # turns = 4
# # while turns > 0:
# #     timmy_the_turtle.forward(100)
# #     timmy_the_turtle.left(90)
# #     turns -= 1
#
# screen = Screen()
# screen.exitonclick()

tim = Turtle()
# tutaj zmieniany tryb kolorow w module a nie w obiekcie
# inaczej RGB nie zadziala
# jako dana wejsciowa moze byc krotka ale nie koniecznie bo inaczej tez dziala
turtle.colormode(255)
# Challenge 2
# for n in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)

# Challenge 3 MOJE
# for n in range(3):
#     tim.color("green")
#     tim.left(120)
#     tim.forward(100)
#
# for n in range(4):
#     tim.color("red")
#     tim.left(90)
#     tim.forward(100)
#
# for n in range(5):
#     tim.color("yellow")
#     tim.left(72)
#     tim.forward(100)
#
# for n in range(6):
#     tim.color("blue")
#     tim.left(60)
#     tim.forward(100)
#
# for n in range(8):
#     tim.color("black")
#     tim.left(45)
#     tim.forward(100)
#
# for n in range(9):
#     tim.color("cyan")
#     tim.left(40)
#     tim.forward(100)
#
# for n in range(10):
#     tim.color("violet")
#     tim.left(36)
#     tim.forward(100)


# Challenge 3 Z KURSU
# color_list = ['red', 'blue', 'yellow', 'green', 'black', 'cyan', 'pink', 'violet', 'orange']
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.left(angle)
#         tim.forward(100)
#
#
# for shape_n in range(3, 11):
#     tim.color(random.choice(color_list))
#     draw_shape(shape_n)


# Challenge 4 MOJE
# color_list = ['red', 'blue', 'yellow', 'green', 'black', 'cyan', 'pink', 'violet', 'orange']
# angle_list = [0, 90, 180, 270]
# tim.pensize(3)
# while True:
#     tim.color(random.choice(color_list))
#     tim.forward(10)
#     tim.left(random.choice(angle_list))

# Challenge 4 Z KURSU
# color_list = ['red', 'blue', 'yellow', 'green', 'black', 'cyan', 'pink', 'violet', 'orange']
# angle_list = [0, 90, 180, 270]
# tim.pensize(5)
# tim.speed("fastest")
#
# def generate_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_tuple = (r, g, b)
#     return rgb_tuple
#
#
# for i in range(200):
#     tim.forward(30)
#     tim.color(generate_color())
#     tim.setheading(random.choice(angle_list))

# Challenge 5 MOJE
# def generate_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_tuple = (r, g, b)
#     return rgb_tuple
#
#
# turn = 0
# tim.speed("fastest")
# while turn != 365:
#     tim.circle(100)
#     tim.setheading(turn)
#     tim.color(generate_color())
#     turn += 5

# Challenge 5 Z KURSU
# def generate_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     rgb_tuple = (r, g, b)
#     return rgb_tuple
#
# 
# def draw_spirograph(size_of_gap):
#     for n in range(int(360 / size_of_gap)):
#         tim.color(generate_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + size_of_gap)
#
# tim.speed("fastest")
# draw_spirograph(5)


screen = Screen()
screen.exitonclick()
