from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __int__(self):
        super(Scoreboard, self).__int__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.score}", False, align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", False, align="center", font=FONT)
