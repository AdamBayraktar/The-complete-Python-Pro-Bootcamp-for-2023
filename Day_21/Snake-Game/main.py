from time import sleep
from snake import Snake
from food import Food
from screen import SnakeScreen
from scoreboard import ScoreBoard, HighScoreBoard
import csv

def main():
    screen = SnakeScreen()   
    the_snake = Snake()
    screen.update()
    food = Food()
    scoreboard = ScoreBoard()
    with open("highscore.csv") as csvfile:
        high_score_reader = csv.reader(csvfile)
        for score in high_score_reader:
            highscore = int(score[0])
            break
    HighScoreBoard(highscore)
    screen.screen.onkeypress(the_snake.turn_left, "Left")
    screen.screen.onkeypress(the_snake.turn_right, "Right")
    screen.screen.onkeypress(screen.bye, "q")
    while True:
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
            if screen.points > highscore:
                update_highscore(screen.points)
            screen.clear()
            main()
            screen.bye()
            return 0
        screen.update()
        sleep(0.1)

   

def update_highscore(new_high_score):
    with open("highscore.csv", "w") as csvfile:
        high_score_writer = csv.writer(csvfile)
        high_score_writer.writerow([new_high_score])


if __name__ == "__main__":
    main()