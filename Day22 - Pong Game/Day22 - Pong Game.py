from turtle import Screen
from pong_paddles import Paddles
from pong_ball import Ball
from pong_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG!")
screen.tracer(0)

paddle_r = Paddles(350)
paddle_l = Paddles(-350)
ball = Ball()
scoreboard_r = Scoreboard(50)
scoreboard_l = Scoreboard(-50)

screen.listen()
screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")

screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    # w momencie wylaczenia animacji caly czas musimy odswiezac ekran inaczej nic sie nie pokaze
    # dlatego jest petla while
    screen.update()
    ball.movement()

    # wykrywanie kolizji z gorna sciana
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # wykrywanie kolizji z paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # wykrywanie kolizji ze sciana boczna
    if ball.xcor() > 380:
        scoreboard_l.display_score()
        ball.reset()
    elif ball.xcor() < -390:
        scoreboard_r.display_score()
        ball.reset()


screen.exitonclick()
