from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, player, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True,) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.shape("square")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.creation(player)

    def creation(self,player):
        if player == 1:
            self.goto(-370,0)
        elif player == 2:
            self.goto(370,0)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
