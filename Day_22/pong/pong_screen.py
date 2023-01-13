from turtle import Screen, Turtle

# class for main screen where game is playing
class PongScreen:

    def __init__(self):
        self.__create()

    def __create(self):
        self.screen = Screen()
        self.screen.setup(width=1000, height=600)
        self.screen.title("Pong Game")
        self.screen.bgcolor("black")
        self.screen.listen()
        self.screen.tracer(0)

    def bye(self):
        self.screen.bye()

    def update(self):
        self.screen.update()






# class for liner drawer
class LineDrawer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.pensize(3)
        self.draw_line()

    def draw_line(self):
        self.penup()
        self.goto(0, -275)
        self.seth(90)
        self.ht()
        for _ in range(56):
            self.pendown() if _ % 2 == 0 else self.penup()
            self.fd(10)

    def win(self):
        self.__summary()
        self.write("You Win!", align="center", font=('System', 38, 'normal'))

    def lose(self):
        self.__summary()
        self.write("Game Over!", align="center", font=('System', 38, 'normal'))

    def __summary(self):
        self.penup()
        self.goto(0, 0)



