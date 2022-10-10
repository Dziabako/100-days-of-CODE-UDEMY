import time
from turtle import Screen
from cross_player import Player
from cross_car import CarManager
from cross_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    # wykrywanie kolizji z autem
    for c in car.all_cars:
        if player.distance(c) < 20:
            game_is_on = False
            scoreboard.game_over()

    # wykrywanie dojscia do konca drogi i resetowanie pozycji
    if player.ycor() > 280:
        player.reset_pos()
        car.move_increase()
        scoreboard.increase_score()

screen.exitonclick()
