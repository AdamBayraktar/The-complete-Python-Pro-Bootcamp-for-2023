from turtle import Turtle
import random

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.shapesize(0.5)
        self.setheading(random.choice([random.randint(130, 220), random.randint(0, 45)]))

    # move at constant pace
    def auto_move(self):
        self.fd(20)


    # if there is any collision change direction
    def change_direction_if_hit(self, user_pos, comp_pos):
        """ Change direction if there is hit with horizontal walls or with paddles and score point if it hit vertical walls
        user_pos: (x, y) - position of user paddle
        comp_pos: (x, y) - position of computer paddle
        """
        # take information from positions
        user_pos_x, user_pos_y = user_pos
        user_pos_x, user_pos_y = round(user_pos_x), round(user_pos_y)
        comp_pos_x, comp_pos_y = comp_pos
        comp_pos_x, comp_pos_y = round(comp_pos_x), round(comp_pos_y)
        # the ball radial is 10
        comp_pos_x = 440
        user_pos_x = -440
        # the length of paddle is 100
        user_range_y = range(user_pos_y - 60, user_pos_y + 60)
        cop_range_y = range(comp_pos_y - 60, comp_pos_y + 60)
        # position of ball
        self.bal_x, self.bal_y = self.position()
        self.bal_x, self.bal_y = round(self.bal_x), round(self.bal_y)
        self.__check_wall()     
        return self.__change_direction(self.__check_comp_hit(comp_pos_x, cop_range_y), self.__check_user_hit(user_pos_x, user_range_y))

   
   # changes ball heading if it hit horizontal walls
    def __check_wall(self):       
        if self.bal_y <= -290:
            if 270 < self.heading() < 360:
                new_heading = 360 - self.heading()
                self.seth(new_heading)
            else:
                new_heading = 180 - (self.heading() - 180)
                self.seth(new_heading)
        elif self.bal_y >= 290:
            if 0 < self.heading() < 90:
                new_heading = 360 - self.heading()
                self.seth(new_heading)
            else:
                new_heading = 180 - (self.heading() - 180)
                self.seth(new_heading)


    # return True if ball is touching comp paddle
    def __check_comp_hit(self, comp_pos_x, cop_range_y):
        if -15 < (comp_pos_x - self.bal_x) <= 5:
            for y in cop_range_y:
                if y == self.bal_y:
                    return True
    
    # return True if ball is touching comp paddle
    def __check_user_hit(self, user_pos_x, user_range_y):
        if 10 >= (user_pos_x - self.bal_x) >= -15:
            for y in user_range_y:
                if y == self.bal_y:
                    return True


    def __change_direction(self, is_hit_user, is_hit_comp):
        if is_hit_user or is_hit_comp:
            self.the_heading = self.heading()
            if 270 < self.the_heading < 360:
                new_heading = 180 + (360 - self.heading()) 
                self.seth(self.random_straight_hit(new_heading))
            elif 180 < self.the_heading < 270:
                new_heading = 0 + (self.heading() - 180)
                self.seth(self.random_straight_hit(new_heading, "right"))
            elif 0 < self.the_heading < 90:
                new_heading = 180 - self.heading()
                self.seth(self.random_straight_hit(new_heading))
            elif 90 < self.the_heading < 180:
                new_heading = 180 - self.heading()
                self.seth(self.random_straight_hit(new_heading, "right"))
            else:
                if self.the_heading <= 90 or self.the_heading >= 270:
                    self.setheading(150)
                else:
                    self.setheading(20)
            return True


    def check_score(self):
        if self.bal_x < -480 or self.bal_x > 480:
            return True

    
    def random_straight_hit(self, normal_heading, direction='left'):
        if direction == 'left':
            normal_lst = [normal_heading for _ in range(5)]
            normal_lst.append(180)
            return random.choice(normal_lst)
        else:
            normal_lst = [normal_heading for _ in range(5)]
            normal_lst.append(0)
            return random.choice(normal_lst)
        