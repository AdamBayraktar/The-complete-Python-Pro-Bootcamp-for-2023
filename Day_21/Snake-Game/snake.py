from turtle import Turtle


class Snake:
    def __init__(self, size=3, color='white'):
        self.color = color
        self.size = 3
        self.__snake = self.__create_snake()


    def __str__(self):
        return self.__snake


    @property
    def snake(self):
        return self.__snake

    # it is first creation of snake. By default it is created by 3 blocks
    def __create_snake(self):
        snakes = []
        pos_x = 0
        for _ in range(self.size):
            snake = self.__create_body_block()
            snake.goto(pos_x, 0)
            snakes.append(snake)
            pos_x -= 20
        return snakes

    # creates 1 snake body block
    def __create_body_block(self):
        body_block = Turtle()
        body_block.color(self.color)
        body_block.shape("square")
        body_block.resizemode("user")
        body_block.turtlesize(stretch_wid = 1, stretch_len=1)
        body_block.penup()
        return body_block

    # increase snake size by one block
    def increase_size(self):
        """ Increase snake size when it eats food
        the_snake - list of objects that creates whole body of snake
        """
        body_block = self.__create_body_block()
        position = self.__snake[-1].position()
        body_block.goto(*position)
        self.__snake.append(body_block)

    # moves snake at constant pace
    def move_snake(self):
        all_pos = []
        for part in self.__snake:
            all_pos.append(part.position())
        for part in range(len(self.__snake) - 1):
            self.__snake[part + 1].goto(*all_pos[part])
        self.__snake[0].fd(20)


    def turn_right(self):
        return self.__snake[0].rt(90)

    def turn_left(self):
        return self.__snake[0].lt(90)



    # check is snake hit the wall
    def is_wall_hit(self):
        cor_x, cor_y = self.__snake[0].position()
        if not (-301 < cor_x < 301 )or not (-301 < cor_y < 301):
            return True

    # check if is body hit
    def is_body_hit(self):
        h_x, h_y = self.__snake[0].position()
        h_x, h_y = round(h_x), round(h_y)
        for body_part in self.__snake[1:]:
            b_x, b_y = body_part.position()
            b_x, b_y = round(b_x), round(b_y)
            if h_x == b_x and b_y == h_y:
                return True