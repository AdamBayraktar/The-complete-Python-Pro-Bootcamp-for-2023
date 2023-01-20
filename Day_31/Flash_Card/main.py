from tkinter import Tk, Button, Canvas, END, PhotoImage
import csv
import random


BACKGROUND_COLOR = "#B1DDC6"

# function that discard card
# red button puts card to the end of word list
# green button just discards card
# ends if it is last card
def put_to_end():
    game_list.append(game_list[0])
    discard_card()



def discard_card():
    game_list.pop(0)
    global flip
    window.after_cancel(flip)
    if game_list:
        cv.itemconfig(card, image=card_front_pic)
        cv.itemconfig(title, text="Spanish", fill="black")
        cv.itemconfig(the_word, text=game_list[0][0], fill="black")
        flip = window.after(4000, flip_card)
        
    else:
        cv.itemconfig(title, text="Congratulation!")
        cv.itemconfig(the_word, text="This was last card. Take a break and come back tomorrow. I am proud of you! <3")
        cv.after(2000, cv.quit)


def flip_card():
    cv.itemconfig(card, image=card_back_pic)
    cv.itemconfig(title, text="English", fill="white")
    cv.itemconfig(the_word, text=game_list[0][1], fill="white")







# create list that holds list of spanish and english word
with open("data/spanish_words.csv", "r", encoding="UTF 8") as file:
    words_dicts = csv.reader(file)
    game_list = []
    for words in words_dicts:
        game_list.append(words)
random.shuffle(game_list)



# General GUI setup
window = Tk()
window.config(bg=BACKGROUND_COLOR, width=1000, height=700)
window.title("Flash Cards")

# create canvas
cv = Canvas(width=1000, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
# create imgae objects
card_front_pic = PhotoImage(file="images/card_front.png")
card_back_pic = PhotoImage(file="images/card_back.png")
card = cv.create_image(500, 300, image=card_front_pic)

cv.place(x=0, y=0)
# create title that describe the language of the word and word objects
title = cv.create_text(500, 140, text="Spanish", fill="black", font=('arial', 20, ''))
the_word = cv.create_text(500, 320, text=game_list[0][0], fill="black", font=('arial', 45, 'bold'))
# cv.itemconfig(card, image=card_back_pic)


# create buttons
wrong_pic = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_pic, highlightthickness=0, activebackground=BACKGROUND_COLOR, bd=0, command=discard_card)
wrong_button.place(x=600, y=570)
right_pic = PhotoImage(file="images/right.png")
correct_button = Button(image=right_pic, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=put_to_end)
correct_button.place(x=300, y=570)

# flip card
global flip
flip = window.after(4000, flip_card)

window.mainloop()