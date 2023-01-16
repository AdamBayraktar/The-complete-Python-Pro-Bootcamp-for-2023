from turtle import Screen


class SnakeScreen:

    def __init__(self):
        self.screen = self.start()
        self.__points = 0


    def start(self):
        screen = Screen()
        screen.title("Classic Snake Game")
        screen.listen()
        screen.setup(width=620, height=620)
        screen.tracer(0)
        screen.bgcolor("black")
        return screen

    def update(self):
        self.screen.update()

    def bye(self):
        self.screen.bye()

    def clear(self):
        self.screen.clear()

    @property
    def points(self):
        return self.__points

    def add_point(self):
        self.__points += 1