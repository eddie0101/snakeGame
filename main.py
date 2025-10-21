from turtle import Screen, Turtle
from snake import Snake
from food import Food
import constants

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(False)

snake = Snake(screen)
food = Food()

# Game state flag
running = True

# Controls
screen.listen()
screen.onkey(lambda: running and snake.up(), "Up")
screen.onkey(lambda: running and snake.down(), "Down")
screen.onkey(lambda: running and snake.left(), "Left")
screen.onkey(lambda: running and snake.right(), "Right")

food.next_cookie()
screen.update()

# Adjust o match the grid
CELL = 20
HIT_RADIUS = CELL * 0.5

def check_food_collision():
    x_s, y_s = snake.get_head_coords()
    x_f, y_f = food.get_coords()
    if abs(x_s - x_f) < 0.1 and abs(y_s - y_f) < 0.1:
        return True

def check_tail_collision():
    x_s, y_s = snake.get_head_coords()
    for segment in snake.segments[1:]:
        x_seg, y_seg = segment.position()
        if abs(x_s - x_seg) < 0.1 and abs(y_s - y_seg) < 0.1:
            return True
    return False

def debug():
    print(f"Snake head coords: {snake.get_head_coords()}")
    print(f"Food coords: {food.get_coords()}")

def game_run():
    global running
    if not running:
        return # stop the loop

    snake.move()

    if check_food_collision(): 
        food.next_cookie()
        snake.grow()

    if check_tail_collision():
        running = False
        gameover()
        screen.update()
        print("collision")
        return # IMPORTANT: do not schedule another timer

    screen.update()
    screen.ontimer(game_run, constants.SNAKE_DEFAULT_SPEED)

def gameover():
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