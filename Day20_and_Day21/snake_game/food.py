from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-330,330), random.randint(-280,280))
