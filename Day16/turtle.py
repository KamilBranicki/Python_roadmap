from turtle import Turtle, Screen

timmy = Turtle() #Turtle to klasa, timmy to object
timmy.shape("turtle")
timmy.color("green")
timmy.shapesize(2,2,2)
timmy.forward(100)
#attr syntax: car.spped
#method syntax: car.stop()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

#https://docs.python.org/3/library/turtle.html - turtle module doc
#https://cs111.wellesley.edu/reference/colors - turtle colors

