from turtle import Turtle
import random
BALL_SPEED = 0.17

class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.color("red")
        self.penup()
        self.start = 0
        self.ball_reset(player = "")

    def first_ball(self):
        player = random.randint(1,2)
        if player == 1:
            self.move_x = -BALL_SPEED
        elif player == 2:  
            self.move_x = BALL_SPEED

    def first_ball_up_down(self):
        up_down = random.randint(1,2)
        if up_down == 1:
            self.move_y = BALL_SPEED
        elif up_down == 2:
            self.move_y = -BALL_SPEED        

    def first_move(self):
        self.start = 1

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce(self, direction):
        if direction == "bounced_from_up":
            self.move_y = -BALL_SPEED  
        elif direction == "bounced_from_down":
            self.move_y = BALL_SPEED
        elif direction == "bounced_from_player1":
            self.move_x = BALL_SPEED
        elif direction == "bounced_from_player2":
            self.move_x = -BALL_SPEED

    def ball_reset(self, player):
        self.goto(0, 0)
        self.first_ball_up_down()
        if player == "for_player_1":
            self.move_x = -BALL_SPEED
        elif player == "for_player_2":
            self.move_x = BALL_SPEED
        else:
            self.first_ball()
