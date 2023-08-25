from turtle import Turtle, Screen
import  random
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

screen = Screen()
screen.title("TURTLES RACE")
screen.setup(width = 500, height = 400)

for turtle_index in range (0,len(colors)):
    turtle = Turtle(shape = "turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(-240, y_positions[turtle_index])
    all_turtles.append(turtle)

user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
user_bet_desc = "User Bet: " + user_bet

bet = Turtle(visible = False)
bet.penup()
bet.goto(0,175)
bet.write(arg = user_bet_desc, align = "center", font = ('Arial', 16, 'bold'))
result = Turtle(visible = False)
result.penup()
result.goto(0,155)
result_str = "The winnner is: "

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 220:
            result_str += turtle.pencolor()
            result.write(arg = result_str, align = "center", font = ('Arial', 16, 'bold'))
            result.goto(0,130)
            if turtle.pencolor() == user_bet:
                result.write(arg = "You WON the bet!", align = "center", font = ('Arial', 16, 'bold'))
            else:
                 result.write(arg = "You LOST the bet!", align = "center", font = ('Arial', 16, 'bold'))
            is_race_on = False
        random_setp = random.randint(0,10)
        turtle.forward(random_setp)

screen.exitonclick()

