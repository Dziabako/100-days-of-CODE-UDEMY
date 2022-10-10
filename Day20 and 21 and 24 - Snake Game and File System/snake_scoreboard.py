from turtle import Turtle

FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(-20, 280)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align="left", font=FONT)

    # zamiast game over jest aktualizacja high score
    def reset_game(self):
        if self.score > self.high_score:
            # bez tej linijki ponizej nie aktualizuje sie high score w czasie rzeczywistym podczas gry
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.display_score()

    def increase_score(self):
        self.score += 1
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", False, align="center", font=("Arial", 15, "normal"))
