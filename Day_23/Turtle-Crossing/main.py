from screen import GameScreen, LeftCar, RightCar
from crazyturtle import CrazyTurtle
from scenery import Road, FinishLine, Level, GameOver
import time
import random


def main():
    # inital game setup
    game_screen = GameScreen()
    turtle = CrazyTurtle()
    # draw roads
    for road_place in range(-200, 210, 90):
        Road(road_place)
    # draw finish line
    FinishLine()
    level = Level()
    game_screen.update()
    # generate some random obstacles
    obstacles = [RightCar(random.randint(-300, 300)), RightCar(random.randint(-300, 300)), RightCar(random.randint(-300, 300)), LeftCar(random.randint(-300, 300)), LeftCar(random.randint(-300, 300)), LeftCar(random.randint(-300, 300))]
    # Turtle movement 
    game_screen.onkeypress(turtle.move_up, "Up")
    game_screen.onkeypress(turtle.move_down, "Down")
    game_screen.onkeypress(turtle.move_left, "Left")
    game_screen.onkeypress(turtle.move_right, "Right")
    # obstacle speed
    speed = 10
    round = 1
    production = 5
    time_sleep = 0.1
    while True:
        # move all obstacles
        for index, car in enumerate(obstacles):
            car.fd(speed)
            if car.outside():
                del obstacles[index]
        time.sleep(time_sleep)
        game_screen.update()
        if turtle.final_line():
            level.level_up()
            turtle.reset()
            if speed < 20:
                speed *= 1.5
            else:
                time_sleep *= 0.9
            if level.level == 5:
                production -= 1
            elif level.level == 10:
                production -= 1
        for car in obstacles:
            if turtle.check_hit(*car.position()):
                GameOver()
                game_screen.update()
                time.sleep(4)
                game_screen.bye()
                return 0
        # create new obstacle
        if round % production == 1:
            obstacles.append(RightCar())
        elif round % production == 2:
            obstacles.append(LeftCar())
        round += 1
        

    

if __name__ == "__main__":
    main()
