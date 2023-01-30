import requests
import json


def get_questions():
    params = {
        "amount": 10,
        "category": 18,
        "type": "boolean"
    }
    questions = requests.get("https://opentdb.com/api.php", params=params).json()
    return questions['results']

question_data = get_questions()