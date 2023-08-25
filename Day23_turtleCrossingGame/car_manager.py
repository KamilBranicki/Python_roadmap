from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self) -> None:
        self.spawned_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # self.creation()

    def creation(self):
        car = Turtle()
        car.color(random.choice(COLORS))
        car.penup()
        car.shape("square")
        car.shapesize(1,2)
        car.goto(315,random.randint(-250,250))
        self.spawned_cars.append(car)
        
    def move(self):
         for car in self.spawned_cars:
              car.goto(car.xcor() - self.car_speed, car.ycor())

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
         