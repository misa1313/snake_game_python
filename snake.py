import turtle


class Snake:
    def __init__(self):
        self.positions = [(0, 0), (-20, 0), (-40, 0)]
        self.ts = []
        self.game_going = True

    def initial_squares(self):
        for i in self.positions:
            t = turtle.Turtle("square")
            t.penup()
            t.pensize(3)
            t.speed(1)
            t.color("white")
            t.goto(i)
            self.ts.append(t)
        return self.ts

    def add_one_more(self):
        t = turtle.Turtle("square")
        t.penup()
        t.hideturtle()
        t.pensize(3)
        t.speed(1)
        t.color("white")
        self.ts.append(t)
        return self.ts

    def move_forward(self):
        for each in range(len(self.ts) - 1, 0, -1):
            p1 = self.ts[each - 1].pos()
            self.ts[each].goto(p1)
            self.ts[each].st()
        self.ts[0].forward(20)
        return self.game_going

    def ts_right(self, angle):
        for each in range(len(self.ts) - 1):
            self.ts[each].right(angle)

    def ts_left(self, angle):
        for each in range(len(self.ts) - 1):
            self.ts[each].left(angle)

    def move(self, direction):
        if direction == "right":
            if self.ts[0].heading() == 0.0:
                self.move_forward()
            elif self.ts[0].heading() == 90.0:
                self.ts_right(90)
            elif self.ts[0].heading() == 270.0:
                self.ts_right(-90)
            else:
                self.game_going = False
        elif direction == "left":
            if self.ts[0].heading() == 180.0:
                self.move_forward()
            elif self.ts[0].heading() == 90.0:
                self.ts_left(90)
            elif self.ts[0].heading() == 270.0:
                self.ts_left(-90)
            else:
                self.game_going = False
        elif direction == "up":
            if self.ts[0].heading() == 0.0:
                self.ts_left(90)
            elif self.ts[0].heading() == 90.0:
                self.move_forward()
            elif self.ts[0].heading() == 180.0:
                self.ts_right(90)
            else:
                self.game_going = False
        elif direction == "down":
            if self.ts[0].heading() == 0.0:
                self.ts_right(90)
            elif self.ts[0].heading() == 270.0:
                self.move_forward()
            elif self.ts[0].heading() == 180.0:
                self.ts_left(90)
            else:
                self.game_going = False
        return self.game_going

    def hit_body(self):
        for each in self.ts[1:]:
            if self.ts[0].distance(each) < 5:
                self.game_going = False

        return self.game_going
