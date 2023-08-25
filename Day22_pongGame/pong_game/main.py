from turtle import Screen
from paddle import Paddle
from ball import Ball
from halfCourt import Half
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

half = Half()
paddle1 = Paddle(player = 1)
paddle2 = Paddle(player = 2)
ball = Ball()
scoreboard = Scoreboard()

direction=""

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")
screen.onkey(ball.first_move, "m")

while scoreboard.score_player2 < 10 and scoreboard.score_player1 < 10:
    screen.update()
    while ball.start == 0:
        time.sleep(1)
        ball.start = 1
    ball.move()

    #Detection of collision with wall
    if ball.ycor() > 280:
        direction="bounced_from_up"
    elif ball.ycor() < -280:
        direction="bounced_from_down"
    #Detection of collision with paddle
    if ball.distance(paddle2) < 40 and ball.xcor() > 355:
        direction="bounced_from_player2"
    elif ball.distance(paddle1) < 40 and ball.xcor() < -360:
        direction="bounced_from_player1"

    ball.bounce(direction=direction)
    #Detection of goal
    if ball.xcor() > 400:
        ball.ball_reset(player = "for_player_2")
        scoreboard.score_player1 +=1
        scoreboard.display()
        ball.start = 0
    elif ball.xcor() < -400:
        ball.ball_reset(player = "for_player_1")
        scoreboard.score_player2 +=1
        scoreboard.display()
        ball.start = 0
    else:
        ball.start = 1

if scoreboard.score_player1 == 10:
    scoreboard.winner = "Left player WON"
elif scoreboard.score_player2 == 10:
    scoreboard.winner = "Right player WON"

scoreboard.game_over()
screen.exitonclick()