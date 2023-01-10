from turtle import Turtle, Screen
import random




def main():
    screen = Screen()
    screen.setup(500, 400)
    the_bet = screen.textinput("Make your bet", "Which turtle will win? ('red', 'orange', 'yellow', 'green', 'blue', 'purple')\n Pick one: ")
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    turtles = []
    cor_y = -100
    for index, the_color in enumerate(colors):
        turtles.append(Turtle(shape="turtle"))
        turtles[index].color(the_color)
        turtles[index].color = the_color
        turtles[index].penup()
        turtles[index].goto(x=-230, y=cor_y)
        cor_y += 40
    
    race = True
    while race:
        for index, turtle in enumerate(turtles):
            random_move(turtle)
            if turtle.xcor() > 220:
                the_winner = turtle.color.title()
                race = False
                break

            
    screen.exitonclick()
    print(f"The winner is {the_winner}")
    if the_bet.title() == the_winner:
        print(f'Your bet was correct! Bravo!')
    else:
        print(f'You bet was incorrect. Maybe next time, you will guess correctly')


def random_move(turtle):
    turtle.fd(random.randint(1, 10))


if __name__ == "__main__":
    main()