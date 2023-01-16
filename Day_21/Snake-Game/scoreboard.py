from turtle import Turtle


class ScoreBoard(Turtle):
    # shows actual score and can also show highscore
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.color("white")
        self.ht()
        self.penup()
        self.goto(-100, 280)
        self.write(f"score: 0", align="center", font=('Arial', 18, 'normal'))

        
    # updates score
    def update_score(self, score):
        self.clear()
        self.write(f"score: {score}", align="center", font=('Arial', 18, 'normal'))

    # shows game over when snake hit wall or body 
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 28, 'normal'))

    



class HighScoreBoard(Turtle):
    # shows actual score and can also show highscore
    def __init__(self, highscore=0):
        super().__init__()
        self.__highscore = highscore
        self.start()

    def start(self):
        self.color("white")
        self.ht()
        self.penup()
        self.goto(100, 280)
        self.write(f"highscore: {self.__highscore}", align="center", font=('Arial', 18, 'normal'))
