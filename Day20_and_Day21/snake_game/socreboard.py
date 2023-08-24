from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible = 0)
        self.score = 0
        with open("C:\Python\Projects\Day20_and_Day21\snake_game\data.txt", mode="r") as file:
            self.high_score = file.read()
        self.high_score = int(self.high_score)
        self.color("white")
        self.penup()
        self.display()

    def display(self):
        self.clear()
        self.goto(0,270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 18, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 26, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.display()