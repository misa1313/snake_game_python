import turtle
import time
from functools import partial
from snake import Snake
from food import Food
from score import Score

game_going = True
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

ts = snake.initial_squares()
screen.update()
ate_food = False
food.newdot()

while game_going:
    screen.update()
    time.sleep(0.1)
    game_going = snake.move_forward()
    screen.listen()
    screen.onkey(key="Right", fun=partial(snake.move, "right"))
    screen.onkey(key="Down", fun=partial(snake.move, "down"))
    screen.onkey(key="Left", fun=partial(snake.move, "left"))
    screen.onkey(key="Up", fun=partial(snake.move, "up"))
    game_going = snake.hit_body()
    x, y = ts[0].pos()
    ate_food = food.showone(x, y)
    if ate_food:
        ts = snake.add_one_more()
        score.score_plus()
        turtle.clear()
    ate_food = False
    if not (-281 <= x <= 281) or not (-281 <= y <= 281):
        game_going = False
    score.score_title()
score.game_over()
turtle.exitonclick()
