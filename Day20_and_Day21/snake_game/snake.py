from turtle import Turtle

STARTING_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POS:
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)

    def add_segment(self):
            snake = Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(self.snake_body[-1].position())
            self.snake_body.append(snake)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]


    def move(self):
        for seg_index in range((len(self.snake_body)-1) , 0 , -1):
            self.snake_body[seg_index].goto(self.snake_body[seg_index-1].position())
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
         if self.head.heading() != UP:           
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:      
            self.head.setheading(LEFT)

    def right(self):
         if self.head.heading() != LEFT:       
            self.head.setheading(RIGHT)