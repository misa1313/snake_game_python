import turtle


class Score:
    def __init__(self):
        self.score = 0

    def score_title(self):
        turtle.color("white")
        turtle.penup()
        turtle.goto(0, 265)
        turtle.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        turtle.hideturtle()

    def game_over(self):
        turtle.goto(0, 0)
        turtle.write("GAME OVER", align="center", font=("Courier", 60, "bold"))

    def score_plus(self):
        self.score += 1
