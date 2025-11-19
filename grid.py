from turtle import Turtle

from constants import SCREEN_WIDTH, CELL_SIZE, SCREEN_LENGTH


class Grid(Turtle):

    def __init__(self):
        super().__init__()
        self.create_grid()

    def create_grid(self):
        self.color("white")

        x1_coord = SCREEN_WIDTH / -2
        y1_coord = SCREEN_LENGTH / -2
        x2_coord = SCREEN_WIDTH / 2
        y2_coord = SCREEN_LENGTH / 2

        for i in range(SCREEN_WIDTH // CELL_SIZE):
            self.penup()
            self.goto(x1_coord + i, y1_coord)
            self.pendown()
            self.goto(x2_coord + i, y2_coord)

