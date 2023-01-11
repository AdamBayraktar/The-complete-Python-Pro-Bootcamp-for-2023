from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.__create_food()


    def __create_food(self):
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.go_to_random_place()
        


    def go_to_random_place(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)

    def is_eaten(self, snake):
        """ chceck if any body part of snake touches food
        snake - the list of objects that creates snake body
        """
        f_x, f_y = self.position()
        f_x, f_y = int(f_x), int(f_y)
        for body in snake:
            head_x, head_y = body.position()
            head_x, head_y = int(head_x), int(head_y)
            head_x_range = range((head_x - 20), (head_x + 20 + 1))
            head_y_range = range((head_y - 20), (head_y + 20 + 1))
            if f_x in head_x_range and f_y in head_y_range:
                return True

