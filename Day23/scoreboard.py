from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.penup()
        self.goto(-220, 270)
        self.level = 1
        self.display()
    
    def display(self):
        self.clear()
        self.goto(-220, 270)
        self.write(arg=f"Level: {self.level}", align="center", font=("Courier", 22, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(arg=f"GAME OVER", align="center", font=("Courier", 26, "bold"))

