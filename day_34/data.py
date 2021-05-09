import requests


def get_questions():
    question_data = []
    response = requests.get(
        "https://opentdb.com/api.php?amount=10&type=boolean")
    response.raise_for_status()
    questions = response.json()["results"]
    for question in questions:
        question_data.append(question)
    return question_data
