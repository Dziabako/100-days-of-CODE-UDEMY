from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = randint(1, 5)
        if chance == 1:
            new_car = Turtle()
            random_y = randint(-250, 250)
            new_car.color(choice(COLORS))
            new_car.shape("square")
            new_car.penup()
            new_car.goto(300, random_y)
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def move_increase(self):
        self.speed += MOVE_INCREMENT
