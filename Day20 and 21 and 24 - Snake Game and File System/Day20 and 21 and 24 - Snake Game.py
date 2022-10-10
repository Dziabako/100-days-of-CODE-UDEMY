from turtle import Screen
from snake_class import Snake
from snake_food import Food
from snake_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game!")
# wylaczenie animacji turtle / jesli jest 0 to nie ma zadnej animacji
# czyli nie ma animacji przemieszczania sie turtle
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    # dzieki temu na ekranie widzimy ze nasz snake porusza sie jako jeden segment
    time.sleep(0.1)
    snake.move()

    # wykrywanie kolizji z jedzeniem (jedzenie ma rozmiar 10x10 dlatego jest 15)
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # wykrywanie kolizji ze sciana
    # nie ma game over wiec wszystko musi sie resetowac od poczatku
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        scoreboard.reset_game()
        snake.reset_snake()

    # wykrywanie kolizji z ogonem
    for body in snake.snakes[1:]:
        if snake.head.position() == body.position():
            scoreboard.reset_game()
            snake.reset_snake()


screen.exitonclick()
