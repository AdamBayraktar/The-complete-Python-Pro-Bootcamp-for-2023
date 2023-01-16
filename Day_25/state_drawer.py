from turtle import Turtle

class StateNameDrawer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()


    def write_name(self, state, x, y):
        self.goto(x, y)
        self.write(f"{state}", align='center', font=('Arial', 8, 'normal'))


    def win(self):
        self.goto(0, 0)
        self.write(f"YOU WIN!", align='center', font=('Arial', 48, 'normal'))


class Counter(StateNameDrawer):
    def __init__(self):
        super().__init__()
        self.goto(350, 250)
        self.score = 0
        self.write(f"{self.score}/50", align='center', font=('Arial', 28, 'bold'))

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}/50", align='center', font=('Arial', 28, 'bold'))