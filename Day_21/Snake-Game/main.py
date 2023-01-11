from time import sleep
from snake import Snake
from food import Food
from screen import SnakeScreen
from scoreboard import ScoreBoard

def main():
    global screen
    screen = SnakeScreen()   
    the_snake = Snake()
    screen.update()
    food = Food()
    scoreboard = ScoreBoard()
    while True:
        control(the_snake)
        the_snake.move_snake()
        if food.is_eaten(the_snake.snake):
            # food.ht()
            screen.add_point()
            food.go_to_random_place()
            the_snake.increase_size()
            scoreboard.update_score(screen.points)
        if the_snake.is_wall_hit() or the_snake.is_body_hit():
            print("Game Over")
            print(f"Your total score is {screen.points}")
            scoreboard.game_over()
            screen.update()
            sleep(2)
            screen.bye()
            return 0
        screen.update()
        sleep(0.1)

   

# controls snake with left and right arrow
def control(the_snake):
    screen.screen.onkeypress(the_snake.turn_left, "Left")
    screen.screen.onkeypress(the_snake.turn_right, "Right")



if __name__ == "__main__":
    main()