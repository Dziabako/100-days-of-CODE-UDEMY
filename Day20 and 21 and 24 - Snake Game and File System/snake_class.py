from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.x_cor = 0
        self.move_distance = 20
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    # nie ma game over wiec po kolizji waz tez musi sie resetowac
    def reset_snake(self):
        # bez tego poprzednie snakei zostana na ekranie a tak przenoszone sa daleko poza obszar gry
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

        # TO BYLA MOJA WERSJA TWORZENIA SNAKE
        # snake = Turtle(shape="square")
        # snake.color("white")
        # snake.penup()
        # snake.goto(self.x_cor, 0)
        # self.x_cor -= 20
        # self.snakes.append(snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)

        self.head.forward(self.move_distance)

    # w ten sposob zapobiegamy mozliwosci cofania sie weza
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
