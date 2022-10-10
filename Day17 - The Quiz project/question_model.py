# NIE WIEM CZY TO JEST DOBRZE ALE Z ZALOZENIA WYBIERA JUZ WCZESNIEJ PYTANIA
# from data import question_data
# from random import choice
#
#
# class Question:
#     def __int__(self):
#         random_question = choice(question_data)
#         self.text = random_question["text"]
#         self.answer = random_question["answer"]

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
