# ROZWIAZANIE Z KURSU JEST NA REPLIT

import turtle as t
import random as r

color_list = [(252, 250, 235), (241, 252, 245), (253, 245, 249), (232, 243, 249), (238, 231, 79), (180, 16, 43),
              (219, 64, 99), (109, 179, 204), (185, 74, 38), (25, 122, 166), (186, 42, 67), (207, 152, 102),
              (22, 136, 85), (188, 176, 23), (20, 31, 68), (216, 130, 154), (70, 170, 100), (19, 166, 208),
              (232, 230, 6), (217, 78, 55), (38, 46, 112), (127, 184, 138), (8, 51, 33), (235, 165, 182),
              (149, 210, 220), (163, 24, 20), (10, 98, 55), (156, 213, 189), (237, 171, 163), (87, 21, 61),
              (6, 87, 107), (85, 12, 8), (115, 118, 151), (174, 184, 217), (248, 11, 27)]


tim = t.Turtle()
screen = t.Screen()
t.colormode(255)


def draw_dots(n_dots):
    for d in range(n_dots):
        tim.dot(20, r.choice(color_list))
        tim.forward(50)


# nie wiem czemu ta pozycja na poczatku ma 20 ale pasuje idealnie w lewy dolny rog
# mozna tez dac inna pozycje
pos_x = 20 - screen.window_width() / 2
pos_y = 20 - screen.window_height() / 2
num_of_dots = 15
rows = 15

tim.penup()
tim.hideturtle()
tim.speed("fastest")

while rows != 0:
    tim.goto(pos_x, pos_y)
    draw_dots(num_of_dots)
    pos_y += 50
    rows -= 1


screen.exitonclick()
