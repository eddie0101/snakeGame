from turtle import Screen, Turtle
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(False)

snake = Snake(screen)
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food.next_cookie()
screen.update()

def check_food_collision():
    if snake.get_head_coords() == food.get_coords():
        food.next_cookie()
        print("##############")

def debug():
    print(f"Snake head coords: {snake.get_head_coords()}")
    print(f"Food coords: {food.get_coords()}")

def game_run():
    snake.move()
    check_food_collision()
    screen.update()
    debug()
    screen.ontimer(game_run, 200)

game_run()

screen.exitonclick()

# comment added on replit