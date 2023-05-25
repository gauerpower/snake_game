from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(x = 0, y = 260)
        self.write(f'Score: {self.score}', True, 'center', ('Courier', 24, 'bold'))

    def increment_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write('Game over.', True, 'center', ('Courier', 24, 'bold'))