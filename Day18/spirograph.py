from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.speed(0)
turtle.colormode(255)
tim.width(2)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tim.circle(150, 360)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()