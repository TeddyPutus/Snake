from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 280)
        self.get_high_score()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 12, 'normal'))

    def update_score(self):
        self.score += 10
        self.write_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over :'(", align="center", font=('Arial', 12, 'normal'))

    def get_high_score(self):
        file = open("high_score.txt", "r")
        self.high_score = int(file.read())
        file.close()

    def save_high_score(self):
        file = open("high_score.txt", "w")
        file.write(f"{self.high_score}")
        file.close()