import random

quiz_questions = {
    "What is the capital of Macau" : "Itself"
}

random_answers = ["Opel", "Stockholm", "Chengdu"]

def quiz_asker (quiz_questions):
    length = len(quiz_question)
    question = random.randint(0,length)
    print(f"{quiz_questions[question]})