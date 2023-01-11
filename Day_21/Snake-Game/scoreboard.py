from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 280)
        self.write("Score: 0", align="center", font=('Arial', 18, 'normal'))

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", align="center", font=('Arial', 18, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 28, 'normal'))