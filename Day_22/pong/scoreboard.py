from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, player="user"):
        super().__init__()
        self.color("white")
        self.player = player
        self.points = 0
        self.hideturtle()
        self.penup()
        self.__start()

    def __start(self):
        self.goto(-100, 230) if self.player == "user" else self.goto(100, 230)
        self.update_score()

    def add_point(self):
        self.points += 1
        self.update_score()

            
    def update_score(self):
        self.clear()
        self.write(self.points, align="center", font=('System', 38, 'normal'))
