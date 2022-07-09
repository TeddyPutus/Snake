from turtle import Turtle

class Snake:

    LENGTH = 3
    SEGMENT_WIDTH = 20

    def __init__(self):
        self.body = []
        for i in range(0, self.LENGTH):
            self.body.append(Turtle())
            self.body[i].shape("square")
            self.body[i].color("white")
            self.body[i].penup()
            self.body[i].setx(i * -20)
        self.head = self.body[0]

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move(self):
        for i in range(self.LENGTH - 1, 0, -1):
            x_position = self.body[i - 1].xcor()
            y_position = self.body[i - 1].ycor()
            self.body[i].goto(x_position, y_position)
        self.body[0].forward(self.SEGMENT_WIDTH)

    def check_collision(self):
        #check collision with self
        for segment in self.body[1:]:
            if segment.distance(self.head) < 10:
                return True
        #check collision with wall
        if self.head.xcor() > 280 or self.head.xcor() < -280 or self.head.ycor() > 280 or self.head.ycor() < -280:
            return True

    def add_segment(self):

        self.LENGTH += 1

        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        self.body.append(segment)

    def reset_snake(self):
        for seg in self.body:
            seg.goto(1000,1000)
        self.move()
        self.body.clear()
        self.__init__()
