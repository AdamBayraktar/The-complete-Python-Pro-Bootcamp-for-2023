from tkinter import Tk, Canvas, Label, Button, PhotoImage
THEME_COLOR = "#375362"

class TriviaQuizGui():
    def __init__(self, quiz_brain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.__start()
        self.next_question()
        self.game = True
        self.window.mainloop()


    # gui initialization
    def __start(self):
        self.window.title("Trivia Questions!")
        self.window.config(background=THEME_COLOR, padx=20, pady=10)
        self.__create_canvas()
        self.__create_score()
        self.__create_true_button()
        self.__create_false_button()


    # create canvas where questions will be displayed
    def __create_canvas(self):
        self.canvas = Canvas(width=400, height=300, highlightthickness=0, bg="white")
        self.question = self.canvas.create_text(200, 150, text="hey", fill=THEME_COLOR, font=("arial", 15, "normal"), width=400, justify="c")
        self.canvas.grid(column=0, columnspan=2, row=1, pady=20)

    # create label that shows true score
    def __create_score(self):
        self.score = Label(text="Score: 0", background=THEME_COLOR, font=("arial", 18, "bold"), fg="white", height=2)
        self.score.grid(column=1, row=0, stick="E")


    # create buttons
    def __create_true_button(self):
        self.the_true_pic = PhotoImage(file="images/true.png")
        self.true = Button(image=self.the_true_pic, highlightthickness=0, activebackground=THEME_COLOR, bd=0, command=self.true)
        self.true.grid(column=0, row=2)
    
    # create false button
    def __create_false_button(self):
        self.the_false_pic = PhotoImage(file="images/false.png")
        self.true = Button(image=self.the_false_pic, highlightthickness=0, activebackground=THEME_COLOR, bd=0, command=self.false)
        self.true.grid(column=1, row=2, pady=30)
    
    # set question    
    def set_question(self, question):
        self.canvas.itemconfig(tagOrId=self.question, text=question)

    # set score
    def set_score(self, score):
        self.score.config(text=f'Score: {score}')
    
    # starts the quiz game
    def next_question(self):
        if self.finish_game():
            self.set_question(self.quiz.next_question())
        else:
            self.set_question(f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.game = False
    # user answered false
    def false(self):
        self.check_answer("false")
    
    
    # user answered true
    def true(self):
        self.check_answer("true")

    def check_answer(self, answer):
        if self.game:
            self.change_bg_color(self.quiz.check_answer(answer))
            self.set_score(self.quiz.score)
            self.next_question()


    def finish_game(self):
        return self.quiz.still_has_questions()

    def change_bg_color(self, color):
        def f():
            self.canvas.config(bg="white")
        self.canvas.config(bg=color)
        self.window.after(200, f)

if __name__ == "__main__":
    gui = TriviaQuizGui()
    gui.set_question("lol")
    gui.window.mainloop()