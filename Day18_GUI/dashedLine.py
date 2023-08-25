from turtle import Turtle, Screen

frank = Turtle()

for i in range(10):
    frank.penup()
    frank.forward(10)
    frank.pendown()
    frank.forward(10)



screen = Screen()
screen.exitonclick()