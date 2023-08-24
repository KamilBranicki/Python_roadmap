from turtle import Screen
from snake import Snake
from food import Food
from socreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=700, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.display()

    #Detect colision with food.
    if snake.head.distance(food) < 15:
        food.refresh()        
        score.score += 1
        snake.add_segment()

    #Detect colision with wall.
    if snake.head.xcor() > 340 or snake.head.xcor() <-340 or snake.head.ycor() > 299 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
        
    #Detect colision with tail.
    for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()
screen.exitonclick()