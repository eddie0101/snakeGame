from turtle import Turtle
import random

from constants import CELL_SIZE

class Food:
    """
    This class is responsible for creating and managing the food that the snake eats.
    """

    def __init__(self, walls):
        self.food = Turtle("circle")
        self.create_food(walls)

    def create_food(self, walls):
        self.food.color("black") # fill color
        self.food.penup()
        self.food.pencolor("yellow") # outline color
        self.food.shapesize(outline=2)
        self.next_cookie(walls)

    def next_cookie(self, walls):
        (up_limit,
         right_limit,
         down_limit,
         left_limit) = walls.get_border_limits()
        self.food.goto(random.randint(left_limit // CELL_SIZE, right_limit // CELL_SIZE) * CELL_SIZE,
                       random.randint(down_limit // CELL_SIZE, up_limit // CELL_SIZE) * CELL_SIZE)
        x_f, y_f = self.get_coords()
        with open("logs.txt", "a") as file:
            file.write(f"Snake: ({x_f}, {y_f})\n")

    def get_coords(self):
        return self.food.position()
