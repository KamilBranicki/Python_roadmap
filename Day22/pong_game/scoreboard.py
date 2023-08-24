from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = False) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.score_player1 = 0
        self.score_player2 = 0
        self.winner = ""
        self.display()

    def display(self):
        self.clear()
        self.goto(0,250)
        self.write(arg=f"{self.score_player1} {self.score_player2}", align="center", font=("Courier", 36, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write(f"{self.winner}", align="center", font=("Courier", 26, "bold"))
