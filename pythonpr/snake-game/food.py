from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

    def refresh(self):
        x_position = random.randint(-280, 280)
        y_position = random.randint(-280, 280)
        self.goto(x_position, y_position)
