from turtle import Turtle

MOVE_DISTANCE = 20
SNAKE_STARTING_LENGTH = 3
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def generate_segment(self, coord):
        snake_segment = Turtle(shape='square')
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.goto(coord)
        self.segments.append(snake_segment)
        
    def create_snake(self):
        for loc in STARTING_COORDINATES:
            self.generate_segment(loc)

    def extend_length(self):
        final_segment_x = self.segments[-1].xcor()
        final_segment_y = self.segments[-1].ycor()
        if self.segments[0].heading() == 90:
            new_x = final_segment_x
            new_y = final_segment_y - 20
        elif self.segments[0].heading() == 180:
            new_x = final_segment_x + 20
            new_y = final_segment_y
        elif self.segments[0].heading() == 270:
            new_x = final_segment_x 
            new_y = final_segment_y + 20
        elif self.segments[0].heading() == 0:
            new_x = final_segment_x - 20
            new_y = final_segment_y
        self.generate_segment((new_x, new_y))

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