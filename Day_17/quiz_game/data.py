import requests


# creates list of dictionaries that have two keys: the question and the answer to it
test = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")

question_data = []

for question in test.json()['results']:
    text = question['question']
    answer = question['correct_answer']
    question_data.append({"text": text, "answer": answer})


