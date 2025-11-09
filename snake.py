from turtle import Turtle
from constants import MOVE_DISTANCE, STARTING_POSITIONS
import globals

class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.segments = []
        self.create_snake()
        self._speed = 1

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    @property
    def speed(self):
        return self._speed

    def speed_increase(self):
        self._speed += 0.1

    def grow(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        
    def get_head_coords(self):
        return self.segments[0].position()

    def up(self):
        if self.segments[0].heading() != 90 and self.segments[0].heading() != 270 and globals.allow_snake_heading_change == True:
            self.segments[0].setheading(90)
        globals.allow_snake_heading_change = False

    def down(self):
        if self.segments[0].heading() != 90 and self.segments[0].heading() != 270 and globals.allow_snake_heading_change == True:
            self.segments[0].setheading(270)
        globals.allow_snake_heading_change = False

    def left(self):
        if self.segments[0].heading() != 0 and self.segments[0].heading() != 180 and globals.allow_snake_heading_change == True:
            self.segments[0].setheading(180)
        globals.allow_snake_heading_change = False

    def right(self):
        if self.segments[0].heading() != 0 and self.segments[0].heading() != 180 and globals.allow_snake_heading_change == True:
            self.segments[0].setheading(0)
        globals.allow_snake_heading_change = False