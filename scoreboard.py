from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.display_score()
        self.hideturtle()

    def display_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 12, "bold"))

    def score_update(self):
        self.score += 1
        self.clear()
        self.display_score()