from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        score_data = open('high_score.txt')
        self.high_score = int(score_data.read())
        score_data.close()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(x = 0, y = 260)
        self.write(f'Score: {self.score} High Score: {self.high_score}', True, 'center', ('Courier', 24, 'bold'))

    def increment_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(x = 0, y = 0)
    #     self.write('Game over.', True, 'center', ('Courier', 24, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            score_data = open('high_score.txt', 'w')
            score_data.write(f'{self.high_score}')
            score_data.close()
        self.score = 0
        self.update_score()