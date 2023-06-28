import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        super().__init__()
        self.cars = []

    def create_car(self, rate):
        if rate % 6 == 0:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move_cars(self, level):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT)
