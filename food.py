from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('green')
        self.speed(10)
        self.goto(x = random.randrange(-280, 280, 20), y = random.randrange(-280, 280, 20))

    def regenerate(self, segments):
        segment_coords = [segment.pos() for segment in segments]
        x = random.randrange(-280, 280, 20)
        y = random.randrange(-280, 280, 20)
        while (x, y) in segment_coords:
            x = random.randrange(-280, 280, 20)
            y = random.randrange(-280, 280, 20)
        self.goto(x, y)
        
