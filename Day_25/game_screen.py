from turtle import Screen


class StateScreen():
    
    def __init__(self):
        self.screen = self.__start()

    
    def __start(self):
        screen = Screen()
        screen.title("US States Game")
        screen.setup(800, 600)
        screen.bgpic("blank_states_img.gif")
        screen.listen()
        screen.tracer(0)
        return screen

    def bye(self):
        self.screen.bye()

    def update(self):
        self.screen.update()