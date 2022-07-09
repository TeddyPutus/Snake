from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):

        #make the right shape, pen up etc.
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")

        self.new_location()
        # #random location on the screen
        # x_cor = randint(-290, 290)
        # y_cor = randint(-290, 290)
        # self.goto(x_cor, y_cor)

    def new_location(self):
        # random location on the screen
        x_cor = randint(-290, 290)
        y_cor = randint(-290, 290)
        self.goto(x_cor, y_cor)