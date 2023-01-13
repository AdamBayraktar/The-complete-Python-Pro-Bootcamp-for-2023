from turtle import Turtle


class CrazyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.seth(90)


    def move_up(self):
        self.fd(30)

    def move_down(self):
        cor_x, cor_y = self.position()
        if cor_y > -260:
            self.goto(cor_x, cor_y - 30)
        else:
            self.goto(cor_x, -280)

    def move_left(self):
        cor_x, cor_y = self.position()
        if cor_x > -360:
            self.goto(cor_x - 30, cor_y)
        else:
            self.goto(-390, cor_y)

    def move_right(self):
        cor_x, cor_y = self.position()
        if cor_x < 360:
            self.goto(cor_x + 30, cor_y)
        else:
            self.goto(383, cor_y)

    def final_line(self):
        return self.ycor() > 280

    def reset(self):
        self.goto(0, -280)

    def check_hit(self, obs_x, obs_y):
        cor_x, cor_y = self.position()
        if abs(cor_x - obs_x) <= 32 and abs(cor_y - obs_y) < 10:
            return True

    
