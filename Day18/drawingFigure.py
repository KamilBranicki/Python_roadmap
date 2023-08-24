from turtle import Turtle, Screen

tim = Turtle()

for i in range (3,10):
    full = 0
    angle = 360 / i
    for j in range(0,i):
        tim.forward(100)
        tim.setheading(tim.heading() + angle)

screen = Screen()
screen.exitonclick()