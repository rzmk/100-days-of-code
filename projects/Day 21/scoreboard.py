from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Open Sans", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
