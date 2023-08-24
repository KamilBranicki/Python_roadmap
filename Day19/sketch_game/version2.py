from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)
screen = Screen()

def move_forward():
        tim.forward(5)
        screen.onkeyrelease(key="w", fun=draw)

def move_backward():
        tim.backward(5)
        screen.onkeyrelease(key="s", fun=draw)

def turn_left():
        tim.setheading(tim.heading() + 10 )
        screen.onkeyrelease(key="a", fun=draw)

def turn_right():
        tim.setheading(tim.heading() - 10 )
        screen.onkeyrelease(key="d", fun=draw)


def clear():
       screen.resetscreen()

screen.listen()
def draw():
    screen.onkeypress(key="w", fun=move_forward)
    screen.onkeypress(key="s", fun=move_backward)
    screen.onkeypress(key="a", fun=turn_left)
    screen.onkeypress(key="d", fun=turn_right)
    screen.onkeypress(key="space", fun=clear)

while True:
     draw()
     screen.exitonclick()

