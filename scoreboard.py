from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.goto(0, 260)
        self.update_scoreboard()

    def game_over(self):
        self.pen.goto(0, 0)
        self.pen.write("GAME OVER", align="center", font=FONT)

    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Level: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

