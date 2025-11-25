from turtle import Turtle
import random

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
        self.food.goto(random.randint(left_limit, right_limit),
                       random.randint(down_limit, up_limit))

    def get_coords(self):
        return self.food.position()
