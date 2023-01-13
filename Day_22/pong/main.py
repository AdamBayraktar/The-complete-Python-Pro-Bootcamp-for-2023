from pong_screen import PongScreen, LineDrawer
from time import sleep
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball


def main():
    # create main playground
    pong_screen = PongScreen()
    # draw dotted lines thorugh half of the playarena
    summary = LineDrawer()
    # display user score
    user_score = ScoreBoard()
    # display computer score
    comp_score = ScoreBoard(player="computer")
    # create user paddle
    user_paddle = Paddle()
    # create computer paddle
    comp_paddle = Paddle("comp")
    # create ball
    ball = Ball()
    # animation is turned off, manually update screen
    pong_screen.update()
    sleep(0.1)
    game_is_on = True
    pong_screen.screen.onkeypress(user_paddle.move_down, "Down")
    pong_screen.screen.onkeypress(user_paddle.move_up, "Up")
    SPEED = 0.03
    game_speed = SPEED
    while game_is_on:
        # auto moves up and down comp paddles, if distance is close than changes to heading toward ball
        comp_paddle.auto_move(ball.position())
        ball.auto_move()      
        pong_screen.update()
        if ball.change_direction_if_hit(user_paddle.position(), comp_paddle.position()):
            game_speed *= 0.99
        if ball.check_score():
            if ball.bal_x < 480:
                comp_score.add_point()
            else:
                user_score.add_point()
            ball.hideturtle()
            ball = Ball()
            game_speed = SPEED

        sleep(game_speed)
        if user_score.points == 3:
            summary.win()
            break
        elif comp_score.points == 3:
            summary.lose()
            break
    pong_screen.update()
    sleep(2)
    pong_screen.bye()


if __name__ == "__main__":
    main()