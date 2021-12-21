from turtle import Turtle
FONT = ('courier', 24, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.penup()
        self.color("White")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()