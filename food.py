from turtle import Turtle
import random

# Note to self: Revise this later to prevent food from generating on top of snake body

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('green')
        self.speed(10)
        self.regenerate()

    def regenerate(self):
        self.goto(x = random.randint(-280, 280), y = random.randint(-280, 280))