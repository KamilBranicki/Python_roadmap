from turtle import Turtle

class Half(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.goto(0,400)
        self.setheading(270)
        self.pencolor("white")
        self.draw()

    def draw(self):
        while self.ycor() > -400:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
