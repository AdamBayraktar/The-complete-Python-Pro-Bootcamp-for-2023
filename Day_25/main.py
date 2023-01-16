from turtle import Turtle, Screen
from game_screen import StateScreen
from state_drawer import StateNameDrawer, Counter
import pandas as pd
import time

def main():
    # read states from csv file
    states = pd.read_csv("50_states.csv")
    # create list of each column
    states_lst = states["state"].tolist()
    x_lst = states["x"].tolist()
    y_lst = states["y"].tolist() 
    # create drawer object that will draw states name on the map
    drawer = StateNameDrawer()  
    # main screen object
    state_screen = StateScreen()
    # object that will count and draw guessed state to total states
    counter = Counter()
    state_screen.screen.onkey(state_screen.bye, "q")
    while True:
        # take user input
        answer = state_screen.screen.textinput("Guess the state", "What's another state name?")
        if answer:
            answer = answer.title()
        else:
            state_screen.bye()
            return 0
        # if answer is correct, display on the map, delete from the lists and update score
        if answer == "Exit":
            df = pd.DataFrame(states_lst, columns=["States"])
            df.to_csv('answers.csv', index=False)
            state_screen.bye()
            return 0
        if answer in states_lst:
            the_index = states_lst.index(answer)
            drawer.write_name(answer, x_lst[the_index], y_lst[the_index])
            states_lst.pop(the_index)
            x_lst.pop(the_index)
            y_lst.pop(the_index)
            counter.update()
        if len(states_lst) < 1:
            drawer.win()
            time.sleep(2)
            state_screen.bye()
            return 0
        state_screen.update()
        time.sleep(1)

        # time.sleep(1)
        state_screen.screen.onkeypress(state_screen.bye, "s")
    state_screen.screen.exitonclick()

if __name__ == "__main__":
    main()