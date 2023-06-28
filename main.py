import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("The turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)
level = 1

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard(level)

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if turtle.ycor() == 290:
        turtle.next_level()
        level += 1
        scoreboard.update_level(level)

    car_manager.create_car(counter)
    car_manager.move_cars(level)
    counter += 1

    for car in car_manager.cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()




