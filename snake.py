from turtle import Turtle

MOVE_DISTANCE = 20
SNAKE_STARTING_LENGTH = 3

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(SNAKE_STARTING_LENGTH):
            snake_segment = Turtle(shape='square')
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.goto(x = 0 - 20 * i, y = 0)
            self.segments.append(snake_segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def turn_north(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def turn_west(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def turn_south(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def turn_east(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)