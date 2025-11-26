from turtle import Turtle

from constants import SCREEN_WIDTH, CELL_SIZE, SCREEN_LENGTH


class Grid(Turtle):

    def __init__(self):
        super().__init__()
        self.create_grid()

    def create_grid(self):
        self.color("white")
        self.pensize(1)

        # coordinates for the first vertical grid line
        x1_coord = CELL_SIZE / 2
        y1_coord = SCREEN_LENGTH / 2
        x2_coord = CELL_SIZE / 2
        y2_coord = SCREEN_LENGTH / -2

        for i in range(SCREEN_WIDTH // 2 // CELL_SIZE):
            self.penup()
            self.goto(x1_coord + i * CELL_SIZE, y1_coord)
            self.pendown()
            self.goto(x2_coord + i * CELL_SIZE, y2_coord)

        x1_coord = CELL_SIZE / -2
        x2_coord = CELL_SIZE / -2
        for i in range(0, -SCREEN_WIDTH // 2 // CELL_SIZE, -1):
            self.penup()
            self.goto(x1_coord + i * CELL_SIZE, y1_coord)
            self.pendown()
            self.goto(x2_coord + i * CELL_SIZE, y2_coord)

        # coordinates for the first horizontal grid line
        x1_coord = SCREEN_WIDTH / -2
        y1_coord = CELL_SIZE / 2
        x2_coord = SCREEN_WIDTH / 2
        y2_coord = CELL_SIZE / 2

        for i in range(SCREEN_LENGTH // 2 // CELL_SIZE):
            self.penup()
            self.goto(x1_coord, y1_coord + i * CELL_SIZE)
            self.pendown()
            self.goto(x2_coord, y2_coord + i * CELL_SIZE)

        y1_coord = CELL_SIZE / -2
        y2_coord = CELL_SIZE / -2
        for i in range(0, -SCREEN_LENGTH // 2 // CELL_SIZE, -1):
            self.penup()
            self.goto(x1_coord, y1_coord + i * CELL_SIZE)
            self.pendown()
            self.goto(x2_coord, y2_coord + i * CELL_SIZE)

        self.hideturtle()

        self.penup()
        self.goto(0, 0)
        self.dot(10, "red")
