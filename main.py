from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

scr = Screen()
scr.setup(width = 600, height = 600)
scr.bgcolor('black')
scr.title('Snake')
scr.tracer(0)
scr.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

scr.onkey(snake.turn_north, 'w')
scr.onkey(snake.turn_west, 'a')
scr.onkey(snake.turn_south, 's')
scr.onkey(snake.turn_east, 'd')

scr.onkey(snake.turn_north, 'Up')
scr.onkey(snake.turn_west, 'Left')
scr.onkey(snake.turn_south, 'Down')
scr.onkey(snake.turn_east, 'Right')

game_going = True

def end_game():
    scoreboard.reset()
    snake.reset()

while game_going:
    scr.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        snake.extend_length()
        food.regenerate(snake.segments)
        scoreboard.increment_score()

    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        end_game()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 15:
            end_game()

scr.exitonclick()