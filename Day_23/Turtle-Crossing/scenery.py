from turtle import Turtle

# blue print for drawing roads
class Road(Turtle):
    def __init__(self, place_y):
        super().__init__()
        self.shape('square')
        # self.resizemode("user")
        self.pensize(60)
        self.color('black')
        self.hideturtle()
        self.place_y = place_y
        self.__draw_road()
        self.__draw_line()

    # draw road
    def __draw_road(self):
        self.penup()
        self.goto(-400, self.place_y)
        self.pendown()
        self.goto(400, self.place_y)

    # draw lines on road
    def __draw_line(self):
        self.penup()
        self.pensize(1)
        self.color('white')
        self.goto(-400, self.place_y)
        self.pendown()
        self.goto(400, self.place_y) 

# draw finish line
class FinishLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.resizemode('user')
        self.penup()
        self.pensize(20)
        self.cor_y = 230
        self.cor_x = -270
        self.seth(0)
        self.shape("square")
        self.color_var = 20
        for row in range(3):
            self.__finish_line()
            if row % 2 == 0:
                self.stamp()


    def __finish_line(self):
        self.goto(self.cor_x, self.cor_y)
        # self.pendown()
        for _ in range(-240, 281, 40):
            self.color("black")
            self.stamp()
            self.penup()
            self.fd(20)
            self.color("white")
            # self.pendown()
            self.stamp()
            self.fd(20)
        self.color("black")
        self.penup()
        self.cor_y += 20
        self.cor_x += self.color_var
        self.color_var *= -1


# class that shows current level and changes if there is level up
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-390, 250)
        self.level = 1
        self.__draw_level()


    def level_up(self):
        self.level += 1
        self.__draw_level()

    def __draw_level(self):
        self.clear()
        self.write(f"Level {self.level}", align='left', font=('Arial', 18, 'normal'))


# writes GAME OVER when game end
class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.hideturtle()
        self.write(f"GAME OVER", align='center', font=('Arial', 40, 'normal'))

