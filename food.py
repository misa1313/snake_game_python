import turtle
import random


class Food:
    def __init__(self):
        self.dot = None
        self.y = None
        self.x = None
        self.ate_one = False

    def newdot(self):
        self.x, self.y = random.randint(-279, 279), random.randint(-279, 279)
        self.dot = turtle.Turtle("circle")
        self.dot.penup()
        self.dot.color("yellow")
        self.dot.setpos(self.x, self.y)

    def showone(self, xcor, ycor):
        if ((xcor >= (self.x - 10)) and (xcor <= (self.x + 10))) and (
                (ycor >= (self.y - 10)) and (ycor <= (self.y + 10))):
            self.ate_one = True
            self.x, self.y = random.randint(-279, 279), random.randint(-279, 279)
            self.dot.setpos(self.x, self.y)
        else:
            self.ate_one = False

        return self.ate_one
