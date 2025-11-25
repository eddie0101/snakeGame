import constants
import settings
from turtle import Turtle

from constants import CELL_SIZE


class Walls:

    def __init__(self):
        self.up_border = 0
        self.down_border = 0
        self.left_border = 0
        self.right_border = 0
        self.create_border()

    def create_border(self):
        self.up_border = constants.SCREEN_LENGTH / 2
        self.down_border = constants.SCREEN_LENGTH / -2
        self.left_border = constants.SCREEN_WIDTH / -2
        self.right_border = constants.SCREEN_WIDTH / 2

        # Adjust borders to be inside the screen
        self.up_border -= 30
        self.down_border += 30
        self.left_border += 20
        self.right_border -= 20

        if settings.PRINT_BORDERS_POSITION:
            print("\nBorders positions:")
            print(f"up_border: {self.up_border}")
            print(f"down_border: {self.down_border}")
            print(f"left_border: {self.left_border}")
            print(f"right_border: {self.right_border}")
        self.show_border()

    def get_border_limits(self):
        return (int(self.up_border - CELL_SIZE),
                int(self.right_border - CELL_SIZE),
                int(self.down_border + CELL_SIZE),
                int(self.left_border + CELL_SIZE))

    def show_border(self):
        wall = Turtle("square")
        wall.color("green")
        wall.pensize(20) 
        wall.penup()
        wall.goto(self.left_border, self.up_border)
        wall.pendown()
        wall.goto(self.right_border, self.up_border)
        wall.goto(self.right_border, self.down_border)
        wall.goto(self.left_border, self.down_border)
        wall.goto(self.left_border, self.up_border)
        return True

    def check_wall_collision(self, snake):
        if (
            self.left_border < snake.get_head_coords()[0] < self.right_border and
            self.up_border > snake.get_head_coords()[1] > self.down_border
        ):
            return False
        return True