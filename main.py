from turtle import Turtle, Screen
from snake import Snake
import time

scr = Screen()
scr.setup(width = 600, height = 600)
scr.bgcolor('black')
scr.title('Snake')
scr.tracer(0)
scr.listen()

snake = Snake()

scr.onkey(snake.turn_north, 'w')
scr.onkey(snake.turn_west, 'a')
scr.onkey(snake.turn_south, 's')
scr.onkey(snake.turn_east, 'd')

game_going = True


while game_going:
    scr.update()
    time.sleep(0.1)
    snake.move()

    

scr.exitonclick()