import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
angles = [0,90,180,270,360]

while True:
    for i in range (0,11):
        tim.speed(0)
        tim.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        tim.setheading(random.choice(angles))
        tim.forward(25)
        tim.width(1+tim.width())
