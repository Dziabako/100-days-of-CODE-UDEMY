from turtle import Turtle
WIDTH = 20
HEIGHT = 100


# w ten sposob nie musimy tworzyc obiektu poniewaz dziediczymy z turtle wszystko
# obiekt sie tworzy wtedy w glownym pliku programu
class Paddles(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_pos, 0)
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
