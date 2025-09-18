from turtle import Turtle
from snake import MOVE_DISTANCE
import random

FOOD_GEN_BOUNDARY = 280
FOOD_SIZE = (int)(FOOD_GEN_BOUNDARY / MOVE_DISTANCE) # food generation boundary

class Food:

  def __init__(self):
    self.food = Turtle("circle")
    self.create_food()

  def create_food(self):
    self.food.color("black") # fill color
    self.food.penup()
    self.food.pencolor("yellow") # outline color
    self.food.shapesize(outline=2)
    self.next_cookie()

  def next_cookie(self):
    self.food.goto(random.randint(-FOOD_SIZE, FOOD_SIZE) * MOVE_DISTANCE, random.randint(-FOOD_SIZE, FOOD_SIZE) * MOVE_DISTANCE) # move food to random location\

  def get_coords(self):
    return self.food.position()