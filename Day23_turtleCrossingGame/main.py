import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("gray")
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")

loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.move()
    loop_counter +=1
    if loop_counter == 6:
        cars.creation()
        loop_counter = 0
    
    #Detection of colision with car
    for car in cars.spawned_cars:
        if player.distance((car.xcor()-10), (car.ycor()- 10)) < 20 or player.distance((car.xcor()), (car.ycor())+5) < 20:
            scoreboard.game_over()
            game_is_on = False

    #Detection of level completition
    if player.ycor() > FINISH_LINE_Y:
        cars.speed_up()
        player.refresh()
        scoreboard.level +=1
        scoreboard.display()
screen.exitonclick()