import question_model
import data
import quiz_brain
from quiz_brain import QuizBrain

# create list that contains question as an object
question_bank = []
for question in data.question_data:
    # create question object and append to the list
    the_question = question_model.Question(question["text"], question["answer"])
    question_bank.append(the_question)

# create game brain
quiz = QuizBrain(question_bank)

# ask quetion as long as there are remaining question
while quiz.still_has_questions():
    quiz.next_question()


# print final statement 
print("You've completed the quiz")
print(f"Your final score was:{quiz.score}/{len(quiz.question_list)}")