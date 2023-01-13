from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, player="player"):
        super().__init__()
        self.color("white")
        self.player = player
        self.penup()
        self.shape("square")
        self.resizemode("user")
        self.seth(90)
        self.turtlesize(0.7, 5)
        self.__take_position()

    def __take_position(self):
        self.goto(-450, 0) if self.player == "player" else self.goto(450, 0)


    def move_up(self):
        cor_x, cor_y = self.position()
        if cor_y < 230:
            # self.fd(80)
            self.goto(-450, cor_y + 80)
        elif cor_y <= 250:
            # self.fd(250 - cor_y)
            self.goto(-450, 250)
    def move_down(self):
        cor_x, cor_y = self.position()
        if cor_y > -230:
            self.bk(80)
        elif cor_y >= -250:
            self.bk(250 - -cor_y)

    def auto_move(self, ball_pos):
        cor_x, cor_y = self.position()
        bal_x, bal_y = ball_pos
        if abs(cor_y - bal_y) < 40 and self.distance(ball_pos) < 400:
            return 0
        elif self.distance(ball_pos) < 400:
            if cor_y > bal_y:
                self.setheading(270)
            elif cor_y < bal_y:
                self.setheading(90)
        elif cor_y >= 250:
            self.setheading(270)
        elif cor_y <= -250:
            self.setheading(90)
        self.fd(20)