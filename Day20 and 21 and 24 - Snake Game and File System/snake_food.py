from turtle import Turtle
import random


# w ten sposob mamy wszystkie metody z klasy Turtle oraz mozemy juz wczesniej ustalic odpowiednie atrybuty
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # w ten sposob zmniejszamy obiekt o polowe
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # w ten sposob pozycja jedzenie bedzie sie odswiezac
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
