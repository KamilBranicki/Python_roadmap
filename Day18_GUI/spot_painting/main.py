# import colorgram

# colors = colorgram.extract('C:\Python\Projects\Day18\spot_painting\spot_painting.jpg', 9)
# colors_list=[]

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     colors_list.append((r, g, b))

import random
import turtle as t

colors_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48)]
marker = t.Turtle()
t.colormode(255)
marker.penup()
marker.hideturtle()
marker.speed(0)
marker.setpos(-225,-225)
x, y = marker.position()

for i in range (0,10):
    marker.setpos(x, y)
    for i in range (0,10):
        marker.dot(20 ,random.choice(colors_list))
        marker.forward(50)
    y += 50

screen = t.Screen()
screen.exitonclick()