"""
This module is the main entry point for the snake game.
"""

from turtle import Screen, Turtle
from snake import Snake
import globals
from food import Food
from scoreboard import Scoreboard
import constants
from walls import Walls
from grid import Grid
import settings

screen = Screen()
screen.setup(constants.SCREEN_WIDTH, constants.SCREEN_LENGTH) # height updated from 600 to 620 in order to have space for displaying the score
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(False)

walls = Walls()
snake = Snake(screen)
food = Food(walls)
scoreboard = Scoreboard()
if settings.DISABLE_GRID:
    grid = None
else:
    grid = Grid()

# Game state flag
running = True

# Controls
screen.listen()
screen.onkey(lambda: running and snake.up(), "Up")
screen.onkey(lambda: running and snake.down(), "Down")
screen.onkey(lambda: running and snake.left(), "Left")
screen.onkey(lambda: running and snake.right(), "Right")

food.next_cookie(walls)
screen.update()

# Adjust to match the grid
CELL = 20
HIT_RADIUS = CELL * 0.5

def check_food_collision():
    """
    Check if the snake head is close enough to the food to be considered a collision.
    :return: True if the snake head is close enough to the food, False otherwise.
    """
    x_s, y_s = snake.get_head_coords()
    x_f, y_f = food.get_coords()
    if abs(x_s - x_f) < 0.1 and abs(y_s - y_f) < 0.1:
        print("inside food collision")
        return True
    return False

def check_tail_collision():
    """
    Check if the snake head is close enough to any segment of the tail to be considered a collision.
    :return: True if the snake head is close enough to any segment of the tail, False otherwise.
    """    
    x_s, y_s = snake.get_head_coords()
    for segment in snake.segments[1:]:
        x_seg, y_seg = segment.position()
        if abs(x_s - x_seg) < 0.1 and abs(y_s - y_seg) < 0.1:
            return True
    return False

def debug():
    """
    Print the coordinates of the snake head and the food.
    :return: None
    """
    print(f"Snake head coords: {snake.get_head_coords()}")
    print(f"Food coords: {food.get_coords()}")

def game_run():
    """
    Main game loop.
    :return: None
    """
    global running
    if not running:
        return # stop the loop

    globals.allow_snake_heading_change = True
    snake.move()

    if check_food_collision():
        scoreboard.score_update()
        food.next_cookie()
        snake.grow()
        snake.speed_increase()

    if check_tail_collision() or walls.check_wall_collision(snake):
        running = False
        gameover()
        screen.update()
        print("collision")
        return # IMPORTANT: do not schedule another timer

    screen.update()
    snake_speed = constants.SNAKE_DEFAULT_SPEED // snake.speed
    screen.ontimer(game_run, int(snake_speed))

def gameover():
    """
    Display game over message and exit the game.
    :return: None
    """
    if settings.DISABLE_GAMEOVER:
        return
    
    # Disable controls
    screen.onkey(None, "Up")
    screen.onkey(None, "Down")
    screen.onkey(None, "Left")
    screen.onkey(None, "Right")

    # Hide all existing turtles (snake, food) so they don't overlap the text
    for t in screen.turtles():
        t.clear()
        t.hideturtle()

    # Show message
    msg = Turtle(visible=False)
    msg.penup()
    msg.color("white")
    msg.goto(0, 10)  # Position in the center
    msg.write("GAME OVER!", align="center", font=("Arial", 24, "bold"))
    msg.goto(0, -20)
    msg.write("Press ENTER key to exit", align="center", font=("Arial", 12))

    # Bind ENTER to close window
    screen.onkey(screen.bye, "Return")
    screen.listen() # make sure key events are active

game_run()
screen.exitonclick()
# comment added on replit