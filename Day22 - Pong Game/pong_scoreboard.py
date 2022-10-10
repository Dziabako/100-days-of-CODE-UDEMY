from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x_cor):
        super(Scoreboard, self).__init__()
        self.x_cor = x_cor
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x_cor, 250)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(f"{self.score}", False, align="center", font=("Courier", 30, "normal"))
        self.score += 1
