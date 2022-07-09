from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

snake_body = []
game_active = True
game_speed = 0.08

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake-a-tron 6000")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()

screen.listen()
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")



while game_active:
    snake.move()
    screen.update()
    time.sleep(game_speed)
    if snake.head.distance(food) < 20:
        food.new_location()
        snake.add_segment()
        scoreboard.update_score()
    if snake.check_collision():
        # game_active = False
        scoreboard.reset_score()
        snake.reset_snake()
        time.sleep(0.5)

scoreboard.game_over()
screen.exitonclick()
