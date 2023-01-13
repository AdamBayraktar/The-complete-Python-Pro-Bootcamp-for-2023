from turtle import Screen, Turtle
import random

class GameScreen:
    def __init__(self):
        self.screen = self.__start()
        self.screen.register_shape("red-car-right.gif")
        self.screen.register_shape("red-car-left.gif")
        self.screen.register_shape("orange-car-right.gif")
        self.screen.register_shape("orange-car-left.gif")
        self.screen.register_shape("green-car-right.gif")
        self.screen.register_shape("green-car-left.gif")
        self.screen.register_shape("pink-car-right.gif")
        self.screen.register_shape("pink-car-left.gif")
        self.screen.register_shape("cyan-car-right.gif")
        self.screen.register_shape("cyan-car-left.gif")
        self.screen.register_shape("blue-car-right.gif")
        self.screen.register_shape("blue-car-left.gif")

    def __start(self):
        screen = Screen()
        screen.title("Crazy Turtle")
        screen.setup(800, 600)
        screen.listen()
        screen.tracer(0)
        return screen

    # quit the game
    def bye(self):
        self.screen.bye()
    # play animation
    def update(self):
        self.screen.update()

    # do action on keypress
    def onkeypress(self, f, key):
        self.screen.onkeypress(f, key)

# general blueprint for obstacle
class Obstacle(Turtle):   
    def __init__(self):
        super().__init__()
        self.penup()

    def outside(self):
        if self.xcor() < -450 or self.xcor() > 450:
            self.ht()
            return True
# blueprint for car that goes to the left
class LeftCar(Obstacle):
    y_pos_left = [176, 86, -4, -184, -94]
    shapes_lefts = ["blue-car-left.gif", "red-car-left.gif", "orange-car-left.gif", "cyan-car-left.gif", "pink-car-left.gif", "green-car-left.gif"]
    def __init__(self, x=420):
        super().__init__()
        self.seth(180)
        self.shape(random.choice(self.shapes_lefts))
        self.goto(x, random.choice(self.y_pos_left))

# blueprint for car that goes to the right
class RightCar(Obstacle):
    y_pos_right = [144, 54, -36, -126, -216]
    shapes_rights = ["blue-car-right.gif", "red-car-right.gif", "orange-car-right.gif", "cyan-car-right.gif", "pink-car-right.gif", "green-car-right.gif"]
    def __init__(self, x=-420):
        super().__init__()
        self.seth(0)
        self.shape(random.choice(self.shapes_rights))
        self.goto(x, random.choice(self.y_pos_right))
        
